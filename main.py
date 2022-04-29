from fastapi import FastAPI
import models

app = FastAPI()


@app.post("/couriers")
def import_couriers(couriers: models.CouriersPostRequest):
    return couriers


@app.get("/couriers/{courier_id}")
def import_couriers(courier_id: int):
    return f"Hey, courier {courier_id}"
