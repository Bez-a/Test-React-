# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:47:28 2023

@author: burgessa3
"""
#### HOW TO RUN THIS CODE IN ANACONDA PROMPT #### -----------------------------

# cd Downloads (or whatever working directory you save this in)
# bokeh serve interactive_pie.py --show 




#### IMPORT STATEMENTS #### ---------------------------------------------------

import math
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure




#### DUMMY FUNCTION #### ------------------------------------------------------

# dummy function that calculates SAF, PtL, and Cjf decimal values using SAF_year, SAF_inf, PtL_year, and PtL_inf slider values 
# you will want to update this to use your actual slider names and the actual mathematical logic 

def dummy(SAF_year_value,SAF_inf_value,PtL_year_value,PtL_inf_value):
    
    # this is just some random math/logic - you'll want to replace this with your actual math/logic for calculating SAF and PtL from the sliders
    # I'm guessing it's that S-curve stuff that goes in here, and you'll want to grab a specific value from that, but I'm not 100% sure
    if SAF_year_value > 2030:
        SAF_value = SAF_inf_value
    else:
        SAF_value = SAF_inf_value / 2
    
    if PtL_year_value > 2030:
        PtL_value = PtL_inf_value
    else:
        PtL_value = PtL_inf_value / 2
    
    
    # this equation is actually valid: Cjf = 1 - (SAF + PtL)
    Cjf_value = 1 - (SAF_value + PtL_value)
    
    #return all the calculated decimal values back to the main code
    return SAF_value, PtL_value, Cjf_value




#### PIE CHART WEDGE SIZE CALCULATION FUNCTION #### ---------------------------

# This function will take in decimal values for SAF, PtL, and Cjf (the outputs from the dummy function)
# It calculates and returns arrays of start and end angles for each wedge of the pie chart
    
def wedge_sizes(SAF_value, PtL_value, Cjf_value):
    
    # place the decimal values for SAF, PtL, and Cfj in an array
    decimals = [SAF_value, PtL_value, Cjf_value]
    
    #convert decimals to percentages
    percentages = [decimals * 100 for decimals in decimals]
    
    #convert the percentages to radians
    radians = [math.radians((percent / 100) * 360) for percent in percentages]


    # create the array that marks the starting angles for each wedge of the pie chart
    # this will start at 0, then each subsequent wedge = previous start angle + angle of current wedge
    start_angles = [math.radians(0)]
    prev = start_angles[0]
    for i in radians[:-1]:
        start_angles.append(i + prev)
        prev = i + prev
    
    
    # create the array that marks the ending angles for each wedge of the pie chart
    # This starts with the second element of the starting angles array and ends with 0 to complete the circle
    end_angles = start_angles[1:] + [math.radians(0)]
    
    
    # return the start_angles and end_angles arrays back to the main code
    return start_angles, end_angles




#### MAIN CODE STARTS HERE #### -----------------------------------------------

# Set default values for some sample SAF and PtL variable sliders. 
# I did SAF_year, SAF_inf, PtL_year, and PtL_inf, but adjust this to suit your needs
default_SAF_year_value = 2025
default_SAF_inf_value = 0.4
default_PtL_year_value = 2030
default_PtL_inf_value = 0.3






# create sliders using those default values
SAF_year_slider = Slider(start=2020, end=2040, value=default_SAF_year_value, step=1, title="SAF year")
SAF_inf_slider = Slider(start=.1, end=.5, value=default_SAF_inf_value, step=.1, title="SAF infusion")
PtL_year_slider = Slider(start=2020, end=2040, value=default_PtL_year_value, step=1, title="PtL year")
PtL_inf_slider = Slider(start=.1, end=.5, value=default_PtL_inf_value, step=.1, title="PtL infusion")


# call the dummy function by using the default values from the sliders 
# it will calculate and return default decimal values for SAF, PtL, and Cjf 
default_SAF_value, default_PtL_value, default_Cjf_value = dummy(default_SAF_year_value,default_SAF_inf_value,default_PtL_year_value,default_PtL_inf_value)


# call the wedge_sizes function using the returned default decimal values for SAF, PtL, and Cjf
# it will calculate and return the start and end angle for each wedge of the pie chart
start_angles, end_angles = wedge_sizes(default_SAF_value, default_PtL_value, default_Cjf_value)


# initialize the source data using the starting and ending angles from wedge_sizes
# this will also set the colors and the legend for each wedge of the pie chart
source = ColumnDataSource(data=dict(
    start=start_angles, 
    end=end_angles, 
    color=['firebrick', 'navy', 'yellow'],
    legend_label=["SAF", "PtL", "Cjf"]
))


# create the plot using the source data
plot = figure()
plot.wedge(x=0, y=0, start_angle='start', end_angle='end', radius=1,
        color='color', alpha=0.6, source=source, legend_label='legend_label')




#### CALLBACK DEF #### --------------------------------------------------------

# callback def that gets run every time either of the sliders is updated

def update(attrname, old, new):
    
    # capture the new values from all the sliders
    new_SAF_year_value = SAF_year_slider.value
    new_SAF_inf_value = SAF_inf_slider.value
    new_PtL_year_value = PtL_year_slider.value
    new_PtL_inf_value = PtL_inf_slider.value
    
    
    # calculate new values for SAF, PtL, and Cjf decimals by calling the dummy function with the new slider values
    new_SAF_value, new_PtL_value, new_Cjf_value = dummy(new_SAF_year_value,new_SAF_inf_value,new_PtL_year_value,new_PtL_inf_value)
    
    
    # call the wedge_sizes function using the new decimal values for SAF, PtL, and Cjf
    # it will calculate and return the new start and end angles for each wedge of the pie chart
    new_start_angles, new_end_angles = wedge_sizes(new_SAF_value, new_PtL_value, new_Cjf_value)
    
    
    # save the new data values back to the source data variable that the plot draws from
    new_data=dict(
    start=new_start_angles, 
    end=new_end_angles, 
    color=['firebrick', 'navy', 'yellow'],
    legend_label=["SAF", "PtL", "Cjf"]
    )

    source.data=new_data




#### MAIN CODE CONTINUES HERE #### -----------------------------------------------


# When any of the slider values change, call the update def
SAF_year_slider.on_change('value', update)
SAF_inf_slider.on_change('value', update)
PtL_year_slider.on_change('value', update)
PtL_inf_slider.on_change('value', update)


# Create the layout that contains all the sliders and the plot
curdoc().add_root(column(SAF_year_slider, SAF_inf_slider, PtL_year_slider, PtL_inf_slider, plot))






