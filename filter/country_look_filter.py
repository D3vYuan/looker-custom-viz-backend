from pydantic import BaseModel

class CountryFilter(BaseModel):
    key: str
    value: str