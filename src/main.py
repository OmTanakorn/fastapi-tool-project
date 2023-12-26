# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import global_config

# Create an instance of FastAPI
app = FastAPI(title=global_config.PROJECT_NAME, debug=global_config.DEBUG)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.auth.router import router as auth_router

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
