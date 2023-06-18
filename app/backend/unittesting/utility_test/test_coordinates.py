import pytest
from app.backend.utility.coordinates import Point, Segment, Grid, create_grid


def test_point_get():
    point = Point(1, 2)
    assert point.get() == (1, 2)

def test_point_str():
    point = Point(1, 2)
    assert str(point) == "Point x:1 y:2"

def test_point_hash():
    point = Point(1, 2)
    assert hash(point) == hash((1, 2))


def test_segment_get():
    points = [Point(1, 2), Point(3, 4)]
    segment = Segment(points)
    assert segment.get() == points

def test_segment_get_raw():
    points = [Point(1, 2), Point(3, 4)]
    segment = Segment(points)
    assert segment.get_raw() == [(1, 2), (3, 4)]

def test_segment_point_in_segment():
    points = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
    segment = Segment(points)
    assert segment.point_in_segment(Point(1, 1)) == True
    assert segment.point_in_segment(Point(3, 3)) == False


def test_grid_split_by_res():
    points = [Point(0, 0), Point(2, 2)]
    segment = Segment(points)
    grid = Grid(segment)
    chunks = grid.split_by_res(1)
    assert len(chunks) > 0

def test_grid_get_centers():
    points = [Point(0, 0), Point(2, 2)]
    segment = Segment(points)
    grid = Grid(segment)
    grid.split_by_res(1)
    centers = grid.get_centers()
    assert len(centers) > 0

def test_grid_remove_missing_values():
    points = [Point(0, 0), Point(2, 2)]
    segment = Segment(points)
    grid = Grid(segment)
    grid.split_by_res(1)
    grid.remove_missing_values()


def test_create_grid():
    points = [Point(0, 0), Point(2, 2)]
    segment = Segment(points)
    grid = create_grid(segment, res_m=1000)
    assert isinstance(grid, Grid)

def test_create_grid_resolution():
    points = [Point(0, 0), Point(2, 2)]
    segment = Segment(points)
    grid = create_grid(segment, res_m=1000)
    assert grid.resolution == 1/111