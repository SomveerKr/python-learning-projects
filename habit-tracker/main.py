import requests
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
pixela_api_endpoint = "https://pixe.la/v1/users"
pixela_api_token = os.getenv("pixela_api_token")
username = "somveer"
graph_id  ="graph1"
headers = {
    "X-USER-TOKEN":pixela_api_token
}
today = datetime.now()
formatted_today = today.strftime("%Y%m%d")
#creating a user:
def create_user():
    user_params = {
        "token":pixela_api_token, "username":username, "agreeTermsOfService":"yes", 
        "notMinor":"yes"
    }
    response= requests.post(pixela_api_endpoint, json=user_params)
    return response

#creating a graph
def create_graph():
    graph_config= {
        "id":"graph1",
        "name":"coding",
        "unit":"hour",
        "type":"float",
        "color":"shibafu"
    }

    graph_endpoint  =  f"{pixela_api_endpoint}/{username}/graphs"

    graph_res = requests.post(graph_endpoint, json=graph_config, headers=headers)
    return graph_res

#post a value to the created graph {graph_id}
def post_to_graph():
    graph_posting_config = {
        "date":formatted_today,
        "quantity":"6.40",
    }
    graph_posting_endpoint = f"{pixela_api_endpoint}/{username}/graphs/{graph_id}"

    posting_res = requests.post(graph_posting_endpoint, json=graph_posting_config, headers=headers)

    return posting_res

#update a graph value
def update_graph():
    update_data = {
        "quantity":"2.10",
    }

    update_endpoint = f"{pixela_api_endpoint}/{username}/graphs/{graph_id}/20250727"

    update_res = requests.put(update_endpoint, json=update_data, headers=headers)

    return update_res

#delete a graph
def delete_graph():
    delete_endpoint = f"{pixela_api_endpoint}/{username}/graphs/workout"

    del_res = requests.delete(delete_endpoint, headers=headers)

    return del_res