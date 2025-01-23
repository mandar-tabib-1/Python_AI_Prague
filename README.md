There are two READMe files. One this way for python module and another is inside the API folder for running the API version of module. 

For python module:
In order to run the AI wind model to obtain wind and turbulence in urban city segment as a result of building-induced turbulence for drone operations.
Read all the points below and then follow it:

 1. For Prague City model - Run the python code with appropriate arguments. Note the date and time arguement has to be upto 2 days in the future.

   python Reconstruc_AI_colab_windspeed_googlecolab.py --date_and_hrs_only '2025-01-21 09:00:00' --threshold_absolute_windspeed_mps 2 --threshold_absolute_turbulence_m2ps2 3

2. User Input: The user input to be provided is "Date and time" (see Step 1 in code) in YYYY-MM-DD HR:min:sec format as shown here - date_and_hrs_only = '2024-10-29 09:00:00'.
   Check if any error message comes on running the above cell. If error, that means put a right date.  The data provided must lie in a future time upto 3 days from now. So, any past dates and any day 3 days after the
   current day in futute IS NOT accepted. The code starts by obtaining the meso-scale wind direction and wind speed for this date and time from an external website, and uses this as input for the AI model. 

3. A OPTIONAL input AI model can take is drone path trajectory in "latitude" and "longitude". But it is needed (NOT MANDATORY).

4. The output of AI code is : 1. wind and turbulence at points within the entire city segment region, and 2. The locations of maximum wind and turbulence location if any can be saved as CSV in folder Results/data_PODY/ as HIGH_WIND_Regions.csv and as HIGH_TURBULENCE_Regions.csv.  The output gets saved as CSV. The user can change the thresholds to decide.

5. AI Methodology : 1. First a training data is generated using computational fluid dynamics simulation for use in training the AI model. The AI model during the training uses an unsupervised machine learning model to 
decompose the training data and find the most dominant spatial patterns. (called basis, which are function of spatial locations) and the accompanying coefficients (which are function of meso-scale wind speed and meso-scale wind direction) for each of the basis.
Then, A radial basis function (RBF) is trained to regress the coefficients to the meso-scale wind speed and meso-scale wind direction using the training data.During inference, for any new meso-scale wind direction and wind speed at the user-provided hour of the day, the AI model then uses the trained RBF function and obtained basis function to
 reconstruct the flow field (wind and turbulence) in entire city segments within few seconds (5-10 s) which is orders of magnitude faster than CFD runs (which can take upto 5 hrs). 

       
