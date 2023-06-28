from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from filter.country_look_filter import CountryFilter
from looker_look_query import LookQuery
from transformation.country_look_transformation import CountryTransformation
from transformation.city_look_transformation import CityTransformation
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/look/{id}/country")
async def get_look(id: int):
    filters={}
    print(f"Look #{id} with {filters}")
    look_query = LookQuery(id, filters)
    look_query_result = look_query.execute()
    country_transformation = CountryTransformation(look_query_result)
    response = country_transformation.processed_message
    return {"description": f"Look #{id} with {filters}",
            "response": f"{response}"}

@app.post("/look/{id}/city")
async def get_look(id: int, filter: CountryFilter):
    filters={filter.key: filter.value}
    filters["all_sessions.city"]="-'(not set)',-'not available in demo dataset'"
    print(f"Look #{id} with {filters}")
    look_query = LookQuery(id, filters)
    look_query_result = look_query.execute()
    city_transformation = CityTransformation(look_query_result)
    response = city_transformation.processed_message
    return {"description": f"Look #{id} with {filters}",
            "response": f"{response}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)

