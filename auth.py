from user import User

# authenticate a user
def authenticate(username, password):

    userAuth = User.find_userName(username)
    if userAuth and userAuth.password == password:
        return userAuth

# identify user from a token
def identity(payload):
    user_id = payload['identity']
    return User.find_userId(user_id)




