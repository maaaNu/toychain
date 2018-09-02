from toycoin import app

@app.route('/transactions', methods=["GET", "POST"])
def transactions():
    return 'Hello, World!'
