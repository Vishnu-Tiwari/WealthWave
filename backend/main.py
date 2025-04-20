from fastapi import FastAPI
app = FastAPI()

@app.get("/transactions")
def get_transactions():
    return {"message": "Transactions will be here"}