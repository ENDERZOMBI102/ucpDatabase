from fastapi import FastAPI
import uvicorn

import database
import root
import packages

db = database.Database()
app = FastAPI()

app.include_router(root.router)
app.include_router(packages.router)


if __name__ == '__main__':
	uvicorn.run( app, host="0.0.0.0", port=8000 )
