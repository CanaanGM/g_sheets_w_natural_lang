from dotenv import dotenv_values
import requests 
config = dotenv_values("./.env")


natrual_lang_url = "https://trackapi.nutritionix.com/v2/"
natrual_lang_excersise_url = f"{natrual_lang_url}natural/exercise"


nutritionix_header = {
    "x-app-id": config.get("NUTRIX_APP_ID"),
    "x-app-key":config.get("NUTRIX_API_KEY")
}

def construct_request_body(query: str):
    return {
        "query": query,
        "gender": "male",
        "weight_kg": 80,
        "height_cm": 174,
        "age":28
    }


def get_exercises_info(query: str) -> list[ dict[str,str]]:
    """calls nutrix natural language API to get exercise info from query string

    Args:
        query (str): the paragraph contains what you did for training ; 500 squats, 2 pushup, 3min sparring.

    Returns:
        list[ dict[str,str]]: list of exercises containing: name, duration, kcal.
    """

    nutral_lang_res = requests.post(
        natrual_lang_excersise_url,
        headers=nutritionix_header, 
        json=construct_request_body(query)
        )
    nutral_lang_res.raise_for_status()
    nutral_lang_res_json = nutral_lang_res.json()
    excersises = nutral_lang_res_json.get("exercises")
    return [ # [ {name:"",dur:"",kcal:""}, {}, . . . ]
        {
            "name":exersise.get("name"),
            "duration":exersise.get("duration_min"), 
            "kcal":exersise.get("nf_calories")
        } for exersise in excersises ]