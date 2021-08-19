from typing import List, Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return "Hello World!"


@app.get("/name/{placeholder}")
async def placeholders(placeholder: Union[str, int], suffix: str=""):
    msg = f"Hello {placeholder}!"
    if suffix:
        msg += f" {suffix}"
    return msg

from enum import Enum

class Database:
    def get_salt_fish(self) -> List[str]:
        return ["saltyboy"]
    
    def get_brackish_fish(self) -> List[str]:
        return ["brackyboy"]
    
    def get_fresh_fish(self) -> List[str]:
        return ["freshyboy"]
    
    def get_all_fish(self) -> List[str]:
        return self.get_salt_fish() + self.get_brackish_fish() + self.get_fresh_fish()

class WaterType(str, Enum):
    salt = "salt"
    brackish = "brackish"
    fresh = "fresh"
    all = "all"

db = Database()

@app.get("/fish")
def get_fish(water_type: WaterType = WaterType.all):
    if water_type == WaterType.salt:
        return db.get_salt_fish()
    elif water_type == WaterType.brackish:
        return db.get_brackish_fish()
    elif water_type == WaterType.fresh:
        return db.get_fresh_fish()
    else:
        return db.get_all_fish()