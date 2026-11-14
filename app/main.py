from fastapi import FastAPI

app = FastAPI(
    title='nothing'
)

@app.get('/health')
def health():
    return {'status' : 'health is ok'}