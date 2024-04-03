from fastapi import FastAPI

app = FastAPI()

@app.get("/hobbits")
async def read_hobbits():
    return ["Frodo Baggins", "Samwise Gamgee", "Peregrin Took", "Meriadoc Brandybuck"]
