#import date and time
from datetime import datetime
import time
import streamlit as st
#times ran global variable
times_ran = 0

# HH:MM used 
mins_used = 0
hours_used = 0

#save the date and compare it to the current date
todaysDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def last_ran():
    last_ran = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if last_ran == todaysDate:
        return "Today"
    else:
        return last_ran

#function to get the date
def get_date():
    return datetime.now().strftime("%Y-%m-%d")  

#function to iterate the times ran
def iterate_times_ran():
    global times_ran
    times_ran += 1

#function to count mins and hours used
def count_mins_used():
    global mins_used, hours_used
    mins_used += 1
    if mins_used == 60:
        hours_used += 1
        mins_used = 0

#function to get the times ran
def get_times_ran():
    return times_ran

#function to get the mins used
def total_time():
    return f"{hours_used} hours and {mins_used} minutes"


    
