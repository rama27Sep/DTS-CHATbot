from fastapi import FastAPI
from api.order_routes import router as order_router

app = FastAPI(title="DTS Chatbot API")

@app.get("/")
def root():
    return {"message": "DTS Chatbot Backend is running 🚀"}

app.include_router(order_router, prefix="/order", tags=["Orders"])
from services.load_from_sqlite import load_orders, load_calibrations
from database.temp_db import temp_db

if __name__ == "__main__":
    load_orders()
    load_calibrations()

    print("\n📦 TEMP DATABASE CONTENTS:")
    print("Orders:", list(temp_db["orders"].values())[:3])  # show first 3
    print("Calibrations:", list(temp_db["calibrations"].values())[:3])
