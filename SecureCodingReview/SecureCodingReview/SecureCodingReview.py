from flask import Flask, request

app = Flask(__name__)

admin_username = "admin"
admin_password = "123456"

users = []

@app.route('/')
def home():
    return "Secure Coding Review Demo"

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    users.append({
        "username": username,
        "password": password
    })

    return "User Registered"

if __name__ == '__main__':
    app.run(debug=True)
