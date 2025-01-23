# Convert module into API. Steps. https://chatgpt.com/c/6790aa6d-69ec-800a-b2ef-8660bb882114 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from obtain_wind_data_for_api import process_wind_data

app = FastAPI()

# Define the data model for incoming requests
class WindDataRequest(BaseModel):
    date_and_hrs_only: str
    threshold_absolute_windspeed_mps: float
    threshold_absolute_turbulence_m2ps2: float

@app.post("/process_wind_data") 
def process_wind_data_endpoint(request: WindDataRequest):  # endpoint is the "entry point" into the API and defines what functionality or data the API provides at that location
    try:
        # Call the refactored function
        csv_path1, csv_path2 = process_wind_data(
            request.date_and_hrs_only,
            request.threshold_absolute_windspeed_mps,
            request.threshold_absolute_turbulence_m2ps2
        )
        if not csv_path1 or not csv_path2:
            raise ValueError("The function returned empty file paths.")
        #if os.path.exists(csv_path1):
            # Return a confirmation with the path to the generated CSV
        #    return {"status": "success", "csv_path": csv_path}
        #else:
            #raise HTTPException(status_code=500, detail="CSV generation failed.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
