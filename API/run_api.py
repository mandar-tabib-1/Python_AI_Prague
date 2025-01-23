import subprocess

# Step 1. Run the FastAPI server using uvicorn web server
subprocess.run(["uvicorn", "API_AI_wind_Prague:app", "--reload", "--host", "127.0.0.1", "--port", "8000"])

# To run this file using command. 
# python run_api.py 

# To run uvicorn web server using command line arguments
#uvicorn api_file_name:app --reload --host 127.0.0.1 --port 8000

#To run uvicorn web server from within a python file.
#if __name__ == "__main__":
#    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
#https://www.uvicorn.org/deployment/