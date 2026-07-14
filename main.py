import os
import requests
from datetime import datetime

X_APP_ID = os.environ.get("X_APP_ID")
X_APP_KEY = os.environ.get("X_APP_KEY")
SHETTY_URL = os.environ.get("SHETTY_URL")
AUTHORIZATION = os.environ.get("AUTHORIZATION")
NUTRITION_URL = "https://app.100daysofpython.dev"
NUTRITION_POST_ENDPOINT = f"{NUTRITION_URL}/v1/nutrition/natural/exercise"
GENDER = "male"
WEIGHT_KG = 57
HEIGHT_CM = 170
AGE = 20

nutrition_headers = {
    "Content-Type": "application/json",
    "x-app-key" : X_APP_KEY,
    "x-app-id" : X_APP_ID
}

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

post_params = {
    "query" : input("Tell me which exercise you did? : "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
nutrition_response = requests.post(url=NUTRITION_POST_ENDPOINT, json=post_params, headers=nutrition_headers)
data = nutrition_response.json()
exercise = data["exercises"][0]["name"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

shetty_params = {
    "workout" : {
        "date" : today_date,
        "time" : today_time,
        "exercise" : exercise,
        "duration" : duration,
        "calories" : calories
    }
}
shetty_headers = {
    "Authorization": AUTHORIZATION,
    "Content-Type": "application/json"
}
shetty_response = requests.post(url=SHETTY_URL,json=shetty_params,headers=shetty_headers)
print(shetty_response.json())
