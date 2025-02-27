from fastapi import FastAPI
from azure.monitor.opentelemetry import configure_azure_monitor
import logging
import os
app = FastAPI()


conn_string = os.getenv("appinsightsKey")

configure_azure_monitor(connection_string=conn_string)
logger = logging.getLogger(__name__)
games_db = [{
    "id": 1,
    "name": "Call of duty:warzone",
    "category":"FPS"
    },
    {
    "id":2,
    "name":"Pubg",
    "category":"FPS"}]
@app.get("/")
async def read_root():
    logger.info("received root request")
    return {"Hello": "World"}

@app.get("/games")
async def read_games():
    logger.info("received games get request")   
    return games_db

@app.post("/games")
async def create_game(game: dict):
    logger.info("received games post request with id as {game.id}")  
    games_db.append(game)
    return game
