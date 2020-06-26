from flask import Flask,jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.admin import AdminLogin,AddCC,AddClub,EventDetails,CCdetails
from resources.CC import CClogin,AddEvent,DeleteEvent,EditEvent,ChangePassword,CCForgotPassword
from resources.users import Registration,UserLogin,Signup,Displayfav,Getdetails,Paid,Unpaid,UserForgotPassword

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
api.add_resource(EventDetails,'/events')
api.add_resource(AddClub,'/clubs')
api.add_resource(CCdetails,'/ccdetails')

api.add_resource(CClogin,'/cclogin')
api.add_resource(AddEvent,'/addevent')
api.add_resource(DeleteEvent,'/deleteevent')
api.add_resource(EditEvent,'/editevent')
api.add_resource(ChangePassword,'/changepassword')
api.add_resource(CCForgotPassword,'/ccforgotpassword')
api.add_resource(Paid,'/paid')
api.add_resource(Unpaid,'/notpaid')

api.add_resource(UserLogin,'/userlogin')
api.add_resource(Signup,'/signup')
api.add_resource(Getdetails,'/eventdetails')
api.add_resource(Displayfav,'/fav')
api.add_resource(Registration,'/registration')
api.add_resource(UserForgotPassword,'/userforgotpassword')

#app.run(port='8055',debug=True)
if __name__=='__main__':
    app.run()
