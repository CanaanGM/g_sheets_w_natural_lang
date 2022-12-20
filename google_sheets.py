from typing import Tuple
from urllib.error import HTTPError
from dotenv import dotenv_values
from datetime import datetime as dt
import requests

config = dotenv_values("./.env")
URL = config.get("GOOGLE_SHEETS_URL")
TOKEN = config.get("TOKEN")
def _construct_datetime() -> Tuple[str,str]:
    """creates and return a tuble with todays date and time

    Returns:
        Tuple[str,str]: today's date, today's time
    """

    today = dt.now()
    time = dt.time(today)
    return (
        f"{today.day}//{today.month}//{today.year}", 
        f"{time.hour}:{time.minute}:{time.second}"
        )


def create_enrty(exercises:list) -> bool:
    current_day, current_time = _construct_datetime()

    # create the request to be sent
    for exercise in exercises:
        name, duration, kcal = exercise.values()

        headers = {
            "Content-Type":"application/json",
            "Authorization": f"Bearer {TOKEN}"
        }

        workout = { # needs to be nested like this . . .
            "workout" : {
                "date": current_day,
                "time": current_time,
                "exercise": name,
                "duration": duration,
                "calories": kcal
            }
        }
        try:
            res = requests.post(URL,headers=headers,  json=workout)
            res.raise_for_status()
        except HTTPError as err:
            print(err) # log it if this goes somewhere . . .
            return False

    return True # execution went swimingly

