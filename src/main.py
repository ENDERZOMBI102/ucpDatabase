from fastapi import FastAPI
import database
import root
import packages

db = database.Database()
app = FastAPI()

app.include_router(root.router)
app.include_router(packages.router)

