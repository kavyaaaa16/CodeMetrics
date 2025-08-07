import httpx

async def fetch_leetcode_stats(username: str):
    url = "https://leetcode.com/graphql"
    query = """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        username
        contestRanking
        profile {
          reputation
          ranking
          userAvatar
        }
        submitStats {
          acSubmissionNum {
            difficulty
            count
            submissions
          }
        }
      }
    }
    """

    variables = {"username": username}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json={"query": query, "variables": variables})
        data = response.json()

        if "errors" in data:
            return None

        user = data.get("data", {}).get("matchedUser", None)
        if user is None:
            return None

        return {
            "username": user["username"],
            "contestRanking": user.get("contestRanking"),
            "profile": user.get("profile"),
            "submissionStats": user.get("submitStats", {}).get("acSubmissionNum", []),
        }
