# backend/app/services/leetcode.py
import httpx
import asyncio

async def fetch_leetcode_stats(username: str):
    url = "https://leetcode.com/graphql"
    query = {
        "query": """
        query getUserProfile($username: String!) {
          matchedUser(username: $username) {
            username
            profile {
              realName
              userAvatar
              ranking
              reputation
              rankingWeekly
            }
            submitStats {
              acSubmissionNum {
                difficulty
                count
              }
            }
          }
        }
        """,
        "variables": {"username": username}
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=query)
        data = response.json()

    if "errors" in data:
        return None  # User not found or error

    user_data = data.get("data", {}).get("matchedUser")
    if not user_data:
        return None

    # You can customize the returned data structure as needed
    stats = {
        "username": user_data["username"],
        "real_name": user_data["profile"]["realName"],
        "ranking": user_data["profile"]["ranking"],
        "reputation": user_data["profile"]["reputation"],
        "weekly_ranking": user_data["profile"]["rankingWeekly"],
        "submissions": {
            entry["difficulty"]: entry["count"]
            for entry in user_data["submitStats"]["acSubmissionNum"]
        }
    }
    return stats
