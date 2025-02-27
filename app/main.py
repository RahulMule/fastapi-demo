from fastapi import FastAPI

app = FastAPI()

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
    return {"Hello": "World"}

@app.get("/games")
async def read_games():
    return games_db

@app.post("/games")
async def create_game(game: dict):
    games_db.append(game)
    return game
