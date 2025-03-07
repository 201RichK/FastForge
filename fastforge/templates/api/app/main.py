from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="{{project_name}}",
    description="FastAPI project generated with FastForge",
    version="0.1.0",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to {{project_name}}! 🚀"}

# Import and include your API routers here
# from app.api.v1 import users, auth
# app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
# app.include_router(users.router, prefix="/api/v1", tags=["users"])
