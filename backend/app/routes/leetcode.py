from fastapi import APIRouter, HTTPException
from app.services.leetcode import fetch_leetcode_stats

router = APIRouter()

@router.get("/user/{username}")
async def get_user_stats(username: str):
    stats = await fetch_leetcode_stats(username)
    if stats is None:
        raise HTTPException(status_code=404, detail="User not found")
    return stats
