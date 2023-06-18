import requests
import geojson
import aiohttp
import asyncio
import tensorflow as tf
from pandas import DataFrame

from app.backend.utility.coordinates import Grid
from app.backend.app.externalAPI.geocode import GeocodioRequests
from app.backend.app.externalAPI.worldpop import load_pops_from_file
from app.backend.app.internalAPI.map_responce import mapResponce

#координати -> перевірка чи кешовано -> якшо ні, то створити грід -> заповнити його через worldpop і geocode -> доповнтити пустуючі значення-> нормалізувати дату в ньому -> кинути грід в map_response

async def load_from_geocode(grid:Grid) -> bool:
    gr = GeocodioRequests()
    await gr.reverse_geocode_async(grid)
    return True

async def load_from_worldpop(grid:Grid) -> bool:
    await load_pops_from_file(grid)
    return True

async def load_from_model(grid:Grid) -> bool:
    mr = mapResponce()
    await mr.predict_from_grid(grid)
    return True