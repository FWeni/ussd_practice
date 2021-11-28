import os
from flask import Flask, request
import requests
from flask import jsonify

app = Flask(__name__)

account1balance = 0
account1availablebalance = 1

account2balance = "20"
account2availablebalance = '20'

@app.route("/balance/<str:accountnumber>", methods = ['POST', 'GET'])
def balance(accountnumber):
    if accountnumber == "first account":
        return jsonify(
            {
                'balance': account1balance,
                'available': account1availablebalance
            }
        )
    elif accountnumber == 'second account':
        return jsonify(
            {
                'balance': account2balance,
                'available': account2availablebalance
            }
        )
    

@app.route('/')
def index():
    return "<h1>Welcome to our server!</h1>"

if __name__ == '__main__':
    app.run(debug=True)