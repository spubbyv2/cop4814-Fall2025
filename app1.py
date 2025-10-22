from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello FIU!'

@app.route('/aboutUs')
def about():
    firstname = "sebas"
    lastname = "medina"
    return f"my name is {firstname} {lastname}"

@app.route('/contact/<string:name>')
def contact(name):
    return f"{name}'s phone number is 123-456-7890"

@app.route('/tekkenPage')
def tekkenPage():
    favGame = "Tekken 8"
    favChar = "Kazuya Mishima"
    return f"My favorite tekken game is {favGame} and {favChar} is my main"

if __name__ == '__main__':
    app.run(debug=True, port=8080)