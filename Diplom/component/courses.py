import requests
from .config import courses_api

money_list = list()

def url_money():
    url = requests.get(courses_api).json()
    return url
    
def data_money():
    for i in url_money():
        money = i["Cur_Abbreviation"]+' '+  str(i["Cur_Scale"]) +' '+ i["Cur_Name"]+' '+  str(i["Cur_OfficialRate"])
        money_list.append(money)   
    return '\n'.join(money_list)
