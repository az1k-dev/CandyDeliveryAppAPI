from fastapi import FastAPI
import models

app = FastAPI()


@app.post("/couriers")
def import_couriers(couriers: models.CouriersPostRequest):
    return couriers
