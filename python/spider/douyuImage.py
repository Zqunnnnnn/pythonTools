import requests
import openpyxl
import os
import uuid

def get_html(url):
    response = requests.get(url)
    html = response.content
    