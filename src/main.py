from fastapi import FastAPI
from typing import Union, Dict, List

app = FastAPI()

database: Union[Dict[str, str], Dict[str, List[str]]]


@app.get("/")
async def root():
	return {"message": "Hello World"}


@app.get('/api/database')
async def getDatabase():
	return database