# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: app04
# @Project: Python-leran-in-total
# @Quelle:

from fastapi import APIRouter, Form
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List, Union, Optional


app04 = APIRouter()

