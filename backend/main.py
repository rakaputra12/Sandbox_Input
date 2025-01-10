from flask import Flask, request, jsonify
from flask_cors import CORS
from instagrapi import Client


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

ACCOUNT_USERNAME = "FarmProjektDHBW"
ACCOUNT_PASSWORD = "FarmProjekt123456"

def custom_manual_input_code(self, username, choice=None):
    print(f"Waiting for security code input for {username} ({choice}) from Fronted...")

'''
    while True:
        print(f"Waiting for security code input for {username} ({choice}):...")
        code = input(f"Enter code (6 digits) for {username} ({choice}): ").strip()

        if code and code.isdigit():
            break
    return code  # is not int, because it can start from 0'''

cl = Client()
cl.challenge_code_handler = custom_manual_input_code(cl, username=ACCOUNT_USERNAME)

cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
print("Logged in successfully!")

if __name__ == "__main__":
    app.run(debug=True, port=5000)