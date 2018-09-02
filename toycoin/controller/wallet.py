import json
import os
from toycoin import app
from flask import jsonify


@app.route('/wallet', methods=['GET', 'POST'])
def wallet():
    with open('wallet.json', 'r') as file:
        wallet = json.load(file)    
    return jsonify(wallet)
 
