import pytest
import asyncio
import tensorflow as tf
from pandas import DataFrame
from app.backend.utility.coordinates import Grid, Segment, Point
from app.backend.app.internalAPI.map_responce import mapResponce


@pytest.fixture
def map_response():
    model_path = "app/backend/ml/model/model.h5"
    return mapResponce(model_path)


@pytest.mark.asyncio
async def test_predict_from_grid(map_response):
    grid = Grid(Segment([Point(99,99),Point(99,99),Point(99,99),Point(99,99)]))
    for i in range(1,4):
        segment = Segment([Point(1, 2), Point(3, 4)])
        segment.data['pop_count_adj'] = 100+i*100
        segment.data['income'] = 50000+i*10000
        grid.chunks.append(segment)

    await map_response.predict_from_grid(grid)

    for chunk in grid.chunks:
        assert chunk.data['crime_level'] != -1
