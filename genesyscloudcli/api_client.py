import profile_handler
import sys
import requests
import base64
import json
import printer
import os

class ApiClient:
    token = ''
    environment = ''
    
    def __init__(self, profile_name=''):
        handler = profile_handler.ProfileHandler()
        profile = handler.get_profile(profile_name)

        self.environment = profile.environment

        auth = profile.client_id +":" + profile.client_secret
        authorization = base64.b64encode(auth.encode())

        request_headers = {
            'Authorization': 'Basic ' + authorization.decode(),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        request_body = {
            'grant_type': 'client_credentials'
        }

        # Get token
        response = requests.post('https://login.{}/oauth/token'.format(profile.environment), data=request_body, headers=request_headers)

        # Get JSON response body
        response_json = response.json()

        self.token = response_json['token_type'] + ' ' + response_json['access_token']




    def post(self, uri, data):
        return self.call_api("POST", uri, data)

    def get(self,uri):
        return self.call_api("GET", uri, None)

    def call_api(self,method, uri, data):
        headers = {
            'Authorization': self.token,
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }

        data_string = ''

        if data != None:
            data_string = json.dumps(data)

        response = requests.request(method, "https://api.{}{}".format(self.environment, uri), data=data_string, headers=headers)
    
        if response.status_code > 200:
            print("{} {}".format(method,uri))
            if data != None:
                printer.print_json(data)
            printer.print_data(response.json())
            exit(1)

        return response.json()

        