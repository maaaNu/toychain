from flask import Flask
app = Flask(__name__)

import toycoin.controller.transactions
import toycoin.controller.wallet