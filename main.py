import requests
from datetime import datetime
import os

APPLICATION_ID = 'd0435597'
APPLICATION_KEY = '8454b41f1372a8ca4c6454752510f60f'
GENDER = 'male'
WEIGHT_KG = '77'
HEIGHT_CM = '178'
AGE = '34'
USER = '87vmehta'
PASSWORD = 'abc123'

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise_text = input('What exercises did you do today?')


headers = {
    'x-app-id': APPLICATION_ID,
    'x-app-key': APPLICATION_KEY,

}

user_config = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=user_config, headers=headers)
results = response.json()
print(results)

today_date = datetime.now().strftime('%d%m%Y')
time = datetime.now().strftime('%X')

for exercise in results['exercises']:
    sheet_input = {
        'workout': {
            'date': today_date,
            'time': time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

sheety_endpoint = 'https://api.sheety.co/0130efe4499aa16e1350d344c98f4674/copyOfMyWorkouts/workouts'
sheet_response = requests.post(url=sheety_endpoint, json=sheet_input, headers=headers, auth=(USER, PASSWORD))
print(sheet_response)