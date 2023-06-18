import pytest
import asyncio
import rasterio
import math
import numpy as np
from app.backend.utility.coordinates import Point, Segment, Grid, create_grid
from app.backend.app.externalAPI.worldpop import load_pops_from_file, _calculate_average, async_range

@pytest.fixture
def example_grid():
    points = [
        Point(0, 0), Point(1, 0), Point(2, 0),
        Point(0, 1), Point(1, 1), Point(2, 1),
        Point(0, 2), Point(1, 2), Point(2, 2)
    ]
    segment = Segment(points)
    grid = Grid(segment)
    grid.split_by_res(1)
    return grid

@pytest.mark.asyncio
async def test_async_range():
    count = 5
    async for i in async_range(count):
        assert i >= 0 and i < count

@pytest.mark.asyncio
async def test_calculate_average():
    cells = {
        10: [0, 0],
        20: [1, 0],
        30: [0, 1],
        40: [1, 1]
    }
    point = Point(0.5, 0.5)
    resolution = 1.0
    expected_result = (10 * (math.sqrt(0.5 ** 2 + 0.5 ** 2) / 1.0) + 
                       20 * (math.sqrt(0.5 ** 2 + 0.5 ** 2) / 1.0) + 
                       30 * (math.sqrt(0.5 ** 2 + 0.5 ** 2) / 1.0) + 
                       40 * (math.sqrt(0.5 ** 2 + 0.5 ** 2) / 1.0)) / len(cells)
    result = await _calculate_average(cells, point, resolution)
    assert result == expected_result

