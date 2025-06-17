from fastapi import APIRouter, Depends, status, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import List
from src.api import auth
import sqlalchemy
from src import database as db

router = APIRouter(
    prefix="/[projects]",
    tags=["projects"],
    dependencies=[Depends(auth.get_api_key)],
)