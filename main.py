import requests
from datetime import datetime
from dotenv import DotEnv

HEIGHT_CM = 185
WEIGHT_KG = 120
AGE = 34
GENDER = "male"

dotenv = DotEnv()
NUTRIONIX_APP_ID = dotenv.get('NUTRI_APP_ID')
NUTRIONIX_API_KEY = dotenv.get('NUTRI_API_KEY')

nutrionix_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrionix_headers = {"x-app-id":NUTRIONIX_APP_ID, "x-app-key":NUTRIONIX_API_KEY}

sheety_end_point = "https://api.sheety.co/2d7d1e4d2143e45a688942d8380eccd2/workoutTracking/workouts"
sheety_token = dotenv.get('SHEETY_TOKEN')
sheety_headers = {"Authorization":f"Bearer {sheety_token}"}

def get_exercise_data(workout):
    nutrionix_params = {
        "query": workout,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    response = requests.post(url=nutrionix_end_point, json=nutrionix_params, headers=nutrionix_headers)
    return response.json()


def post_workout_data(exercise):
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")
    name = exercise["exercises"][0]["name"]
    duration = exercise["exercises"][0]["duration_min"]
    calories = exercise["exercises"][0]["nf_calories"]
    params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }
    response = requests.post(url=sheety_end_point, json=params, headers=sheety_headers)
    print(response.json())

exercise_input = input("Tell me which exercises you did: ")
post_workout_data(get_exercise_data(exercise_input))