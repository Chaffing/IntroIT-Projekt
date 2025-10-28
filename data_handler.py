import json



def load_data(): #tar in datan från data.json, anävnds bara i main
    with open('data.json', "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data: object) -> None: #sparar/uppdaterar data.json, används bara i main
    with open('data.json', "w", encoding="utf-8") as f:
        return json.dump(data, f, ensure_ascii=False, indent=4)

def overwrite_data(all_categories_dict): # skriver över data.json nya lexikon, anävnds bara utanför main
    data = {"questions": all_categories_dict}
    with open('data.json', "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4) 