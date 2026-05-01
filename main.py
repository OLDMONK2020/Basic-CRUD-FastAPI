from fastapi import FastAPI

app = FastAPI()

@app.get('/root')
async def getBooks():
    return {'name':'The secret'}