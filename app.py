import streamlit as st
import os, sys, json
from fpdf import FPDF
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import runtimes as rt
from extra_streamlit_components import TabBar




#get todays date and save it
import datetime
lasttime = rt.last_ran()
ttl = rt.total_time()
#set the mins and hours used to 0
rt.mins_used = 0
rt.hours_used = 0
