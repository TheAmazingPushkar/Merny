from fastapi import FastAPI, status

app = FastAPI(
    title="Rent a Room API",
    description="This is a simple API for renting a room.",
    version="1.0.0",
    contact={"name": "The JR Company", "email": "info@jrcompany.com"},
)


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello, World!"}


@app.get("/rooms", status_code=status.HTTP_200_OK)
def get_rooms():
    apartments = {
        "id": 1,
        "name": "Cozy Apartment",
        "location": "Downtown",
        "price": 1200,
        "available": True,
    }
    return apartments
