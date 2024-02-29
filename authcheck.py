import requests
import json

def idpw():
    link = "https://sheets.googleapis.com/v4/spreadsheets/18DIdGEQF6GVuFl_xGgJMEVmVbxrEDNZy7gRd8EPhro0/values/Sheet1!A2:C2?key=AIzaSyAe7rEqZPxsYoqrATSgL1GNsrFaJMga254"
    f = requests.get(link)
    data=json.loads(f.text)
    userid = data['values'][0][0]
    userpw = data['values'][0][1]
    return [userid, userpw]