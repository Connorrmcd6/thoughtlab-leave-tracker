import streamlit as st
import numpy as np
import pandas as pd
from gspread_dataframe import set_with_dataframe
import gspread
from google.oauth2 import service_account
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


# function to create api connection to google sheets
@st.cache_resource(max_entries = 1,)
def connect_to_gs(_service_account_key):
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = service_account.Credentials.from_service_account_info(_service_account_key, scopes=scopes)
    gs_connection = gspread.authorize(credentials)
    return gs_connection