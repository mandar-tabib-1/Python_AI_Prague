#!/usr/bin/env python
import argparse
import subprocess
import sys

# Function to install missing libraries
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required libraries
required_libraries = ["numpy", "pandas","pyvista==0.43.3","mplcursors==0.5.3","vtk==9.3.1","Pillow==9.3.0"]
for lib in required_libraries:
    try:
        __import__(lib)        
    except ImportError:
        install(lib)
        #__import__(lib)

import os,sys

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))  # Get the directory of the current script
#current_dir = os.getcwd()    # Get the current directory.
print(current_dir)
os.chdir(current_dir) 

sys.path.append(current_dir) #Append to path so that libimport library is detected.
fn2=os.path.join(current_dir, 'Results','data_POD') #Define path to store the results.

sys.path.append(fn2)

import libimport
import pandas as pd
import math
import numpy as np
import random
import requests


# # Demonstration based on user input

def main():
    # ### Step 1. USER INPUT of TIME : DATE AND HOURS in 'YYYY-MM-DD HR:MIN:SEC' FORMAT for wind prediction.
    # #### Input should be for future time upto 3 days
    #date_and_hrs_only = '2025-01-21 09:00:00'# YY-MM-DD HR:MIN:SS 
    parser = argparse.ArgumentParser(description="A script that takes inputs from the command line.",
                                      epilog="Example: python Reconstruc_AI_colab_windspeed_googlecolab.py --date_and_hrs_only '2025-01-21 09:00:00' --threshold_absolute_windspeed_mps 2 --threshold_absolute_turbulence_m2ps2 3")
    

    # Add arguments
    parser.add_argument("--date_and_hrs_only", type=str, help="Enter as a string  in the format 'YY-MM-DD HR:MIN:SS'. For Example: '2025-01-21 09:00:00'", required=True)  # A required string argument
    parser.add_argument("--threshold_absolute_windspeed_mps", type=float, help="Threshold for wind speed in mps", required=True)    # A required integer argument
    parser.add_argument("--threshold_absolute_turbulence_m2ps2", type=float, help="Threshold for wind speed in m2ps2",required=True )      # An optional string argument
    #parser.add_argument("--verbose", action="store_true", help="Enable verbose output")  # A flag argument

    # Parse the arguments
    args = parser.parse_args()

    # Access the arguments
    #if args.verbose:
        
    #    print("Verbose mode is enabled.")
    print( f"Hello, You entered: {args.date_and_hrs_only} with a "
        f"threshold of {args.threshold_absolute_windspeed_mps} mps for wind and "
        f"a threshold of {args.threshold_absolute_turbulence_m2ps2} m2ps2 for turbulence.")

    
    #Manually input parameters in code instead of from command line arguments    
    # date_and_hrs_only = input("Please enter date and hrs as a string in the format 'YY-MM-DD HR:MIN:SS'. For Example: '2025-01-21 09:00:00'. :  ")
    #threshold_absolute_windspeed_mps=3  #in m/s - added based on request from   threshold_absolute_windspeed_mps,threshold_absolute_turbulence_m2ps2
    #threshold_absolute_turbulence_m2ps2=2 #in m2/s2 - added based on request from 
    
    date_and_hrs_only = args.date_and_hrs_only
    threshold_absolute_windspeed_mps=args.threshold_absolute_windspeed_mps   #in m/s - added based on request from   threshold_absolute_windspeed_mps,threshold_absolute_turbulence_m2ps2
    threshold_absolute_turbulence_m2ps2=args.threshold_absolute_turbulence_m2ps2  #in m2/s2 - added based on request from  
  
     
     
  
    # 
    # ### Step 2. USER INPUT of DRONE TRAJECTORY : LATITUDE AND LONGITUDE AS LIST.
    # #### Input latitude and longitude should be within the min and maximum range mentioned below. Otherwise - code will throw error as AI is not trained outside this.
    #For Demo : 10 randomly generated points within the following maximum and minimum.
    random_seed_gen=101
    random.seed(random_seed_gen)
    # Define the minimum and maximum values for latitude and longitude
    min_latitude = 50.04585949932427
    max_latitude = 50.053957709673476
    min_longitude = 14.430968123655077
    max_longitude = 14.444980676344922

    # Generate 10 random latitude and longitude values within the specified range

    random_coordinates = [(random.uniform(min_latitude, max_latitude),\
                        random.uniform(min_longitude, max_longitude))\
        for _ in range(10)]


    # ### Step 3: RUN AI Model using the user-defined inputs to obtain wind field and turbulence in parts of prague.
    Macroscale_ws_wd_prediction, wind_data_near_drone_trajectory,locations_at_high_turbulence,locations_at_high_wind_magnitude,merged_dataframe_U_k_Relative_2_vertiport_reconstructed=libimport.demo(random_coordinates,date_and_hrs_only,fn2,threshold_absolute_windspeed_mps,threshold_absolute_turbulence_m2ps2,API_KEY = 'fa3e3882b6508618a835169fb753d745',visualization=False,absolute_thres=True)

    # ## $\color{green}{\text{Result 1 below.  "wind\_data\_near\_drone\_trajectory" DataFrame}} $
    #  #### " This Dataframe shows following things at provided drone trajectories:
    # - #### latitude,longitude : Specified user-input locations of drone trajectory (input).
    # - #### X,Y,Z : Corresponding "distance in meters from the vertiport" for the location.
    # - #### All Column names are variables : (Turbulent Kinetic Energy (TKE), Velocity_magnitude,  Velocity components (Velocity_X,Velocity_Y, Velocity_Z) and Normalized Velocity_mag and Normalized_TKE ) at the specified drone locations . "
    # - > ###### Normalized variables between 0 to 1. Value of 1 in normalized variable means high value of TKE or velocity at that location while 0 means lowest value.


    wind_data_near_drone_trajectory.loc[:, wind_data_near_drone_trajectory.columns != "Velocity_Magnitude"]

    # ## $\color{green}{\text{Result 2 below.  "locations\_at\_high\_turbulence" DataFrame}} $
    #  #### " This Dataframe shows locations within the computational domain where turbulence is high (> 0.95 normalized TKE values). The column name below refers to : "
    # - #### latitude,longitude : lat,long of region with high normalized tke.
    # - #### X,Y,Z : Corresponding "distance in meters from the vertiport" for the location.
    # - #### All Column names are variables : (Turbulent Kinetic Energy (TKE), Velocity_magnitude,  Velocity components (Velocity_X,Velocity_Y, Velocity_Z) and Normalized Velocity_mag and Normalized_TKE ) at the maximum high turbulence drone locations . "
    # - > ###### Normalized variables between 0 to 1. Value of 1 in normalized variable means high value of TKE or velocity at that location while 0 means lowest value.
    def file_create(file_path):
        if os.path.exists(file_path):
        # Delete the file
            os.remove(file_path)
            print(f"Old file {file_path} has been deleted.")
        else:
            print(f"File {file_path} does not exist so will be created.")
            
    file_path = fn2+'/HIGH_TURBULENCE_Regions.csv'
    file_create(file_path)
    file_path1 = fn2+'/HIGH_WIND_Regions.csv'
    file_create(file_path1)
        
    if locations_at_high_turbulence.empty:
        print(" ")
        print("NO HIGH TURBULENCE regions for the given absolute threshold. User can change the absolute threshold and re-run if they want.")
        
    else:
        print(" ")
        print("THERE ARE Regions that exhibhit TURBULENCE higher than the specified absolute threshold. These are as follows:")
        print("locations_at_high_turbulence")
        columns_to_exclude = ['X', 'Y', 'Z','Velocity_X_', 'Velocity_Y_', 'Velocity_Z_']
        new_column_order = ['latitude', 'longitude', 'Z','tke', 'Normalized_turbulence'] #'Velocity_mag','Normalized_Velocity'
         #.drop(columns=columns_to_exclude)
        print(locations_at_high_turbulence[new_column_order])
        # Save DataFrame to a CSV file at a specified path
        
        locations_at_high_turbulence[new_column_order].to_csv(file_path, index=False)  # index=False to avoid saving the row indices
        print(f"File saved as : {file_path}")
        print( " ")
        
    if locations_at_high_wind_magnitude.empty:
        print(" ")
        print("NO HIGH WIND MAGNITUDE regions for the given absolute threshold. User can change the absolute threshold and re-run if they want.")
    else:
        print(" ")
        print("THERE ARE Regions that exhibhit WIND MAGNITUDE that is higher than the specified absolute threshold. These are as follows:")
        print("locations_at_high_wind_magnitude")
        new_column_order1 = ['latitude', 'longitude', 'Z','Velocity_mag','Normalized_Velocity']
        print(locations_at_high_wind_magnitude[new_column_order1])  
        
        locations_at_high_wind_magnitude[new_column_order1].to_csv(file_path1, index=False)  # index=False to avoid saving the row indices 
        print(f"File saved as : {file_path1}")
        print( " ")
  
    

    

    #print("Macroscale_ws_wd_prediction")
    #print(Macroscale_ws_wd_prediction)

    #print("wind_data_near_drone_trajectory")
    #print(wind_data_near_drone_trajectory[['latitude','longitude','Velocity_mag']])


if __name__ == "__main__":
    main()