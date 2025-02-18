from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "My anme is Faizan ul Haq Sheikh i21-1771"



if __name__ == '__main__':
    app.run(debug=True)
