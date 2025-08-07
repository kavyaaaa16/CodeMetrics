from fastapi import FastAPI
from app.routes import leetcode  # import the router

app = FastAPI()

# include the LeetCode API routes under /api/leetcode
app.include_router(leetcode.router, prefix="/api/leetcode")

@app.get("/")
async def root():
    return {"message": "Backend is running!"}
