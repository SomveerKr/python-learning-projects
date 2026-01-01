import requests
from datetime import datetime

import os
from dotenv import load_dotenv

# This line loads the environment variables from the .env file
load_dotenv()

today = datetime.now()

#bearer token
headers = {"Authorization": f"Bearer {os.getenv("SHEETY_BEARER_TOKEN")}"}

def process_natural_txt_nutritionix():
    req_query = input("Enter your phsical activity: ")
    req_config = {    
        "query": req_query
    }

    req_headers ={
        "x-app-id":os.getenv("NUTRITIONIX_APP_ID"),
        "x-app-key":os.getenv("NUTRITIONIX_API_KEY"),
    }
    url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    res= requests.post(url_endpoint, json=req_config, headers=req_headers)
    return res

def get_data_from_sheety():
    url_endpoint  = f"https://api.sheety.co/{os.getenv("GOOGLE_SHEET_ENDPOINT")}/myWorkouts/workouts"
    res = requests.get(url_endpoint)
    print(res.json())
# get_data_from_sheety()

def post_data_to_sheety():
    nutritionix_res = process_natural_txt_nutritionix()
    exercises_data = nutritionix_res.json()["exercises"]
    exercises = [
        {
            "name":excercise["name"],
            "duration_min":excercise["duration_min"],
            "nf_calories":excercise["nf_calories"]
        } for excercise in exercises_data
    ]
    print(exercises)
    url_endpoint  = f"https://api.sheety.co/{os.getenv("GOOGLE_SHEET_ENDPOINT")}/myWorkouts/workouts"
    for excercise in exercises:
        body ={
            "workout":{
                "date":today.strftime("%d/%m/%Y"),
                "time":today.time().strftime("%X"),
                "exercise":excercise["name"].title(),
                "duration":excercise["duration_min"],
                "calories":excercise["nf_calories"]
            }
    
    }
    #Basic auth
    # post_res = requests.post(url_endpoint, json=body, auth=(os.getenv("USERNAME"), os.getenv("PASSWORD")))
    #using bearer token
    post_res = requests.post(url_endpoint, json=body, headers=headers)
    print(post_res.text) 
post_data_to_sheety()