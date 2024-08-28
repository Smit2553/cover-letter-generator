from typing import Union
import os
from fastapi import FastAPI
from processes.tasks import main

app = FastAPI()


@app.get("/")
async def read_root():
    return (
        {
            "Hello": "World",
            "os": os.name,
        }
    )


@app.get("/generate_doc")
async def run_tasks():
    await main()
    return {"message": "Cover letter generated successfully"}
