import requests
from gohighproject import settings

def contact():
    url = "https://rest.gohighlevel.com/v1/contacts"

    payload = {}#"{\n    \"tags\": [\n        \"n\",\n        \"in dolore esse dol\"\n    ]\n}"
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkpOVEpTV04ya0tkRVZkMElFbEZhIiwiY29tcGFueV9pZCI6ImJmb1Q3MkNWcm9oMlg4ZWZPUmdRIiwidmVyc2lvbiI6MSwiaWF0IjoxNjYxNDE2NzQzNTcxLCJzdWIiOiJQcVJEWDZqMjdXempXRUNsQm92eCJ9.u6WPtyudfB9R4nLnLbBZ6i9KquDeK6WnIOZxKAeE9Hg'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

def contact_id(pk):
    url = "https://rest.gohighlevel.com/v1/contacts/"+str(pk)

    payload = {}#"{\n    \"tags\": [\n        \"n\",\n        \"in dolore esse dol\"\n    ]\n}"
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkpOVEpTV04ya0tkRVZkMElFbEZhIiwiY29tcGFueV9pZCI6ImJmb1Q3MkNWcm9oMlg4ZWZPUmdRIiwidmVyc2lvbiI6MSwiaWF0IjoxNjYxNDE2NzQzNTcxLCJzdWIiOiJQcVJEWDZqMjdXempXRUNsQm92eCJ9.u6WPtyudfB9R4nLnLbBZ6i9KquDeK6WnIOZxKAeE9Hg'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.json(),"resss")
    return response.json()


def cust_field(pk):
    print(pk,"Inside cust pkkkkkk")
    url = "https://rest.gohighlevel.com/v1/custom-fields/"+str(pk)
    print(url,"url")

    payload = {}
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkpOVEpTV04ya0tkRVZkMElFbEZhIiwiY29tcGFueV9pZCI6ImJmb1Q3MkNWcm9oMlg4ZWZPUmdRIiwidmVyc2lvbiI6MSwiaWF0IjoxNjYxNDE2NzQzNTcxLCJzdWIiOiJQcVJEWDZqMjdXempXRUNsQm92eCJ9.u6WPtyudfB9R4nLnLbBZ6i9KquDeK6WnIOZxKAeE9Hg'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.json(),"response.json()")
    return response.json()

def cust_field_put(pk,name):
    url = "https://rest.gohighlevel.com/v1/custom-fields/"+str(pk)
    payload = {
        "name": name,
        "fieldKey": "contact."+str(name),
        "dataType": "TEXT"
    }
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkpOVEpTV04ya0tkRVZkMElFbEZhIiwiY29tcGFueV9pZCI6ImJmb1Q3MkNWcm9oMlg4ZWZPUmdRIiwidmVyc2lvbiI6MSwiaWF0IjoxNjYxNDE2NzQzNTcxLCJzdWIiOiJQcVJEWDZqMjdXempXRUNsQm92eCJ9.u6WPtyudfB9R4nLnLbBZ6i9KquDeK6WnIOZxKAeE9Hg'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.json())
    return response.json()
