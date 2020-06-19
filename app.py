from flask import Flask,jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.admin import AdminLogin,AddCC,AddClub,eventdetails,ccdetails
from resources.CC import CClogin,add_event,delete_event,edit_event,change_password
from resources.users import Registration,userLogin,signup,displayisfav,getdetails

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
api.add_resource(eventdetails,'/events')
api.add_resource(CClogin,'/cclogin')
api.add_resource(AddClub,'/clubs')
api.add_resource(ccdetails,'/ccdetails')

api.add_resource(userLogin,'/userlogin')
api.add_resource(signup,'/signup')
api.add_resource(getdetails,'/event_details')
api.add_resource(displayisfav,'/fav')
api.add_resource(Registration,'/registration')

api.add_resource(add_event,'/add_event')
api.add_resource(delete_event,'/delete_event')
api.add_resource(edit_event,'/edit_event')
api.add_resource(change_password,'/change_password')



#app.run(port='8055',debug=True)
if __name__=='__main__':
    app.run()
