import requests
from datetime import datetime

#----------------------------- CREATE AN ACCOUNT -------------------------------#

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "" #Create your own username
TOKEN = "" #Create your own token

PARAMETERS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

HEADERS = {
    "X-USER-TOKEN": TOKEN
}


#--------------------------------- CREATE GRAPH ----------------------------------#

GRAPH_ID = "coding-graph"
GRAPH_PARAMETERS = {
    "id": GRAPH_ID,
    "name":"CODING",
    "unit":"hrs",
    "type":"float"
    ,"color":"ajisai"
}

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
GRAPH_RESPONSE = requests.put(url = GRAPH_ENDPOINT, json= GRAPH_PARAMETERS, headers= HEADERS)


#--------------------------------- CREATE PIXELS ----------------------------------#

TODAY = datetime.now()

PIXEL_PARAMETERS = {
    "date": TODAY.strftime("%Y%m%d"),
    "unit": "hrs",
    "quantity": input("How many hours did you code today?")
}

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
PIXEL_RESPONSE = requests.post(url=PIXEL_ENDPOINT, json = PIXEL_PARAMETERS, headers= HEADERS)
print(PIXEL_RESPONSE.text)


#--------------------------------- UPDATE A PIXEL ----------------------------------#

#UPDATE_ENDPOINT= f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#NEW_PIXEL_DATA= {
#    "quantity": "4"
# }
#UPDATE_PIXEL = requests.put(url = UPDATE_ENDPOINT, json= NEW_PIXEL_DATA, headers= HEADERS)


#--------------------------------- DELETE A PIXEL ----------------------------------#

#DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')"
#DELETE_PIXEL = requests.delete(url = DELETE_ENDPOINT, headers= HEADERS)










