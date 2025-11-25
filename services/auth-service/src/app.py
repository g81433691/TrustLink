from flask import Flask, jsonify, request

# make flask application instance
app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # get the json data from the request body
    data = request.get_json()  

    # grabbing the username and pass
    username = data.get('username')
    password = data.get('password')

    # just for now until i gain a deeper understanding of 
    # how i want to structure things ill just return the success, theres no db yet
    return jsonify({
        'message': 'User has been succesfully registered!', 
        'username': username
    }), 201  # created

# the login end point - accepting username/pass from end user
# just returning a fake token until i get a better understanding of how i wanna structure
@app.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    return jsonify ({
        'message': 'login succesful',
        'token': 'fake-jwt-token-342523',
        'username': username

    }), 200

# end point for getting a user by ID
@app.route('/user/<user_id>', methods = ['GET'])
def get_user(user_id):

    # making <user_id> a function param
    # just faking user fata for now
    return jsonify({
        'id': user_id,
        'username': f'user_{user_id}',
        'email': f'user_{user_id}@example.com'

    }),200

# end point for deleting user by ID
@app.route('/user/<user_id>', methods = ['DELETE'])
def delete_user(user_id):
    # just simulating deletion
    return jsonify ({
        'message': f'User {user_id} deleted succesfully'
    }), 200

@app.route('/health', methods =(['GET']))
def health_check():

    # this just return JSON response
    return jsonify({
        'status': 'healthy',
        'service': 'auth-service'
    }), 200

if __name__== '__main__': 

    app.run(debug=True, host='0.0.0.0', port=5001)