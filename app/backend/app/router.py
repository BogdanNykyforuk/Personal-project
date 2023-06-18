from app.backend.app.db.mongo_db import Mongo
from fastapi import APIRouter, HTTPException
from typing import Optional


router = APIRouter()
mongo_client = None

@router.on_event("startup")
async def startup_event():
    global mongo_client
    mongo_client = Mongo()
    await mongo_client.test()

@router.get("/")
async def ping():
    return {"Success": True}

@router.get("/db/")
async def ping_db():
    return await mongo_client.test()

@router.get("/db/get_data_from_bounds")
async def get_data_from_bounds(l: float, b: float, r: float, t: float, page: int, time: Optional[int] = 12):
    """
    Retrieve map data within the specified bounds.

    Arguments:
    - l (float): The left boundary value.
    - b (float): The bottom boundary value.
    - r (float): The right boundary value.
    - t (float): The top boundary value.
    - page (int): page number.
    - time (int): time to adjust the values

    Returns:
    - json: A json containing the result of the query.

    Raises:
    - HTTPException(400): If the bounds or time is invalid.
    """
    bounds = (l, b, r, t)
    if (len(bounds) != 4 or
        bounds[2] - bounds[0] < 0 or 
        bounds[3] - bounds[1] < 0
        ):
        raise HTTPException(status_code=400, detail="Invalid bounds")
    if not time in list(range(24)):
        raise HTTPException(status_code=400, detail="Invalid time")
    res = await mongo_client.get_in_bounds(bounds, page, time)
    if res == -1:
        return []
    return res
