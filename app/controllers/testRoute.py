from app import app

@app.route('/', methods=['GET'])
def TestRoute():
    return 'Hello world!', 200