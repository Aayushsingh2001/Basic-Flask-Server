from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Niki (I LOVE YOU SOO MUCH) Darling....'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)