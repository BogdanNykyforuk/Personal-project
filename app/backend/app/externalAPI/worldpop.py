import requests
import geojson
import rasterio
import asyncio
import numpy as np
import math
import asyncstdlib

from app.backend.utility.coordinates import Point, Segment, Grid, create_grid

async def _get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    # print(f'x1:{x1}, x2:{x2}, y1:{y1}, y2:{y2}, point1{point1}, point2{point2}')
    # print(f'x2-x1:{(x2 - x1)}, y2-y1:{(y2 - y1)}, sqx:{(x2 - x1) ** 2}, sqy:{(y2 - y1) ** 2}, math.sqrt:{math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)}\n')
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


async def _calculate_average(cells, point:Point, resolution):
    result = 0
    # print(f'cell len:{len(cells)}')
    # print(f'{cells}\npoint{point}\n')
    for data, cords in cells.items():
        if data<0:
            data = 0
        
        distance = await _get_distance(cords, [point.x, point.y])
        # print(f'{distance}')
        # print(f'cords:{cords}, points:{[point.x, point.y]}, data:{data}')
        result += data * (distance / resolution) / len(cells)
        # print(f'distance:{distance}, dis/res:{(distance / resolution)}, /len:{data * (distance / resolution)}, res+={data * (distance / resolution) / len(cells)}\n')
    # print(f'result:{result}\n')
    # print('-'*40)
    # print('\n')
    return result

async def async_range(stop, start=0, step=1):
    if stop:
        range_ = range(start, stop, step)
    else:
        range_ = range(start)
    for i in range_:
        yield i
        await asyncio.sleep(0)

async def load_pops_from_file(grid:Grid):
    try:
        with rasterio.open("pop_data_small.tif") as src:
            image = src.read(1)
            bounds = (-90, 30, -68, 44)
            resolution = (src.res[0] + src.res[1]) / 2
            step = (abs(bounds[2] - bounds[0])/np.shape(image)[0] + abs(bounds[3] - bounds[1])/np.shape(image)[1]) / 2

        tasks = []
        # print(resolution)
        async for i in async_range(len(grid.chunks)):
            top_left_x = int(abs(grid.chunks[i].center.x - bounds[0])//step) # top_left index
            top_left_y = int(abs(grid.chunks[i].center.y - bounds[3])//step)  # top_left index
            # print(f'tlx:{top_left_x}, tly:{top_left_y}')
            task = asyncio.create_task(_calculate_average({
                image[top_left_x, top_left_y]: [bounds[0] + top_left_x * step, bounds[3] - top_left_y * step],
                image[top_left_x + 1, top_left_y]: [bounds[0] + (top_left_x + 1) * step, bounds[3] - top_left_y * step], 
                image[top_left_x + 1, top_left_y + 1]: [bounds[0] + (top_left_x + 1) * step, bounds[3] - (top_left_y + 1) * step], 
                image[top_left_x, top_left_y + 1]: [bounds[0] + top_left_x * step, bounds[3] - (top_left_y + 1) * step]
            }, grid.chunks[i].center, resolution))

            tasks.append(task)

        results = await asyncio.gather(*tasks)

        for i, result in enumerate(results):
            grid.chunks[i].raw_data['pop_count_adj'] = result
        grid.data_bounds['pop_count_adj'] = [np.ma.masked_less(image, 0.1).min(), np.max(image)]

    except FileNotFoundError as e:
        raise ValueError(f"Tif file was not found! Check path for errors.\n{e}")
