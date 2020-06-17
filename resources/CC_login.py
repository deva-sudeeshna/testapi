from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query
import smtplib 
from email.message import EmailMessage


class User_cc():
    def __init__(self,user_id,password):
        self.user_id=user_id
        self.password=password

    @classmethod
    def getUserByuser_id(cls,user_id):
        res=query(f"""SELECT user_id,password FROM login_details WHERE user_id='{user_id}'""",return_json=False)
        if len(res)>0:  return User_cc(res[0]['user_id'],res[0]['password'])
        return False

class CClogin(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('user_id',type=int,required=True,help="user_id cannot be left blank!")
        parser.add_argument("password",type=str,required=True,help="password cannot be left blank!")
        data=parser.parse_args()
        user=User_cc.getUserByuser_id(data['user_id'])
        if user and safe_str_cmp(user.password,data['password']):
            access_token=create_access_token(identity=user.user_id,expires_delta=False)
            return {"message":"ALLOW ACCESS !!"},200
        return {"message":"Invalid Credentials!"}, 401 

