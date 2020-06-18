from flask import Flask,jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.admin import AdminLogin,AddCC,AddClub
from resources.CC import CClogin,add_event


app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['JWT_SECRET_KEY']='coscskillup'
api=Api(app)
jwt=JWTManager(app)

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request does not contain an access token."
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401

api.add_resource(AdminLogin,'/login')
api.add_resource(AddCC,'/addcc')
api.add_resource(CClogin,'/cclogin')
api.add_resource(AddClub,'/clubs')
api.add_resource(add_event,'/addevent')



app.run(port='8055',debug=True)
'''if __name__=='__main__':
    app.run()'''
