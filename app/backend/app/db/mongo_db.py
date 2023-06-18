import numpy as np
from asyncio import run, create_task, gather

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import ASCENDING

from dotenv import load_dotenv
import os

from app.backend.utility.coordinates import Point, Segment, Grid, create_grid
from app.backend.app.map_request_former import load_from_geocode, load_from_worldpop, load_from_model

class Mongo:
    def __init__(self) -> None:
        self.__uri = self.__load_uri()
        self.client = MongoClient(self.__uri, server_api=ServerApi('1'))
        self.mapdb = self.client.map['map']
        self.page_size = 1000
        self._cr_by_h = self.__get_crimerate_by_hour()

    def __load_uri(self) -> str:
        load_dotenv()
        return f"mongodb+srv://admin:{os.getenv('MONGODB_URI_PSW')}@srmapcluster.fb8xt9p.mongodb.net/?retryWrites=true&w=majority"
    
    def __get_crimerate_by_hour(self):
        cl = [45.3, 37.8, 26.6, 18.6, 15.1, 15.9, 20.2, 28.4, 30.5, 34.6, 38.0, 45.1, 40.0, 43.2, 47.6, 50.9, 54.5, 58.4, 59.1, 61.9, 63.0, 61.0, 54.5, 49.9]
        avg = sum(cl)/len(cl)
        return [i/avg for i in cl]

    async def __post_object(self, item, db:list):
        existing_doc = next((i for i in db if i['cords']['vert'] == item['cords']['vert']), None)
        if existing_doc is None:
            return item
        elif (existing_doc['data']['pop_count_adj'] == -1
                or existing_doc['data']['income'] == -1
                or existing_doc['data']['crime_level'] == -1
                ):
            update_query = {
                '$set': {
                    'data.pop_count_adj': existing_doc['data']['pop_count_adj'] if existing_doc['data']['pop_count_adj'] == -1 else item['data']['pop_count_adj'],
                    'data.income': existing_doc['data']['income'] if existing_doc['data']['income'] == -1 else item['data']['income'],
                    'data.crime_level': existing_doc['data']['crime_level'] if existing_doc['data']['crime_level'] == -1 else item['data']['crime_level']
                }
            }
            self.mapdb.update_one({'id': existing_doc['id']}, update_query)

    async def post_grid(self, grid:Grid):
        data = await grid.to_json()
        # self.mapdb.create_index([('cords.center', ASCENDING)], name='cent_indx')
        tasks = []
        document = self.mapdb.find({})
        for item in data:
            tasks.append(create_task(self.__post_object(item, document)))
        res = await gather(*tasks)
        self.mapdb.insert_many(res)
        # self.mapdb.drop_index('cent_indx')
    
    # def get_2d_map_data(self):
    #     map_data = self.mapdb.find({})
    #     return map_data

    # async def load_to_grid(self):
    #     map_data = list(self.mapdb.find({}))
    #     bounds = {}
    #     bounds['left'] = min([e['cords']['center']['lon'] for e in map_data])
    #     bounds['right'] = max([e['cords']['center']['lon'] for e in map_data]) 
    #     bounds['bottom'] = min([e['cords']['center']['lat'] for e in map_data]) 
    #     bounds['top'] = max([e['cords']['center']['lat'] for e in map_data]) 
    #     grid = Grid(Segment([Point(bounds['left'], bounds['top']), Point(bounds['right'], bounds['bottom']), Point(-bounds['right'], bounds['top']), Point(bounds['left'], bounds['bottom'])]))
    #     grid.resolution = map_data[0]['resolution']
    #     for e in map_data:
    #         pass
    
    async def get_in_bounds(self, bounds:tuple, page:int, time:int=12):
        """
        Filters the map_data based on the provided bounds and returns a new dictionary, consisting of 1000 enteries.

        Arguments:
        bounds (tuple): A tuple with values (left, bottom, right, top).
        map_data (list): A list of dictionaries containing map data.
        page (int): which segment of data to return.

        Returns:
        dict: A new dictionary with filtered coordinates, data sorted by place and resolution in meeters.
        -1: if page number is invalid
        """

        md =  list(self.mapdb.find({}))
        if len(md) < self.page_size * page or self.page_size < 0:
            return -1
        if len(md) < self.page_size * (page + 1):
            map_data = md[self.page_size * page:]
        else:
            map_data = md[self.page_size * page:self.page_size * (page+1)]
        res = []

        for item in map_data:
            cords = item['cords']
            center_lon = cords['center']['lon']
            center_lat = cords['center']['lat']
            
            if bounds[0] <= center_lon <= bounds[2] and bounds[1] <= center_lat <= bounds[3]:
                center = {
                    'lon': center_lon,
                    'lat': center_lat
                }
                
                res.append({
                    'center': center,
                    'data': (item['data']['crime_level'] * self._cr_by_h[time]),
                    'resolution': item['resolution']
                })

        return res
    
    async def test(self):
        try:
            self.client.admin.command('ping')
            return "MongoDB connection succsesful!"
        except Exception as e:
            return e

if __name__ == "__main__":
    m = Mongo()
    m.test()

    grid = create_grid(Segment([Point(-76.7, 39.1), Point(-76.5, 38.6), Point(-76.5, 39.1), Point(-76.7, 38.6)]), 1000)
    print(len(grid.chunks))
    
    # run(load_from_geocode(grid))
    run(load_from_worldpop(grid))
    print(grid.data_bounds['pop_count_adj'])
    print("Loading succsesful!")
    grid.remove_missing_values()
    grid.normalize_data()
    print("Normalization succsesful!")
    print(grid.data_bounds['pop_count_adj'])

    run(load_from_model(grid))

    # run(m.post_grid(grid))
    print("Succsesfuly posted data!")