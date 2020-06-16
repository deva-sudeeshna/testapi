from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query

class User():
    def __init__(self,admin_id,password):
        self.admin_id=admin_id
        self.password=password

    @classmethod
    def getUserByadmin_id(cls,admin_id):
        result=query(f"""SELECT admin_id,password FROM admin WHERE admin_id='{admin_id}'""",return_json=False)
        if len(result)>0:  return User(result[0]['admin_id'],result[0]['password'])
        return False

class AdminLogin(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('admin_id',type=int,required=True,help="Admin_id cannot be left blank!")
        parser.add_argument("password",type=str,required=True,help="password cannot be left blank!")
        data=parser.parse_args()
        user=User.getUserByadmin_id(data['admin_id'])
        if user and safe_str_cmp(user.password,data['password']):
            access_token=create_access_token(identity=user.admin_id,expires_delta=False)
            return {"message":"ALLOW ACCESS !!"},200
        return {"message":"Invalid Credentials!"}, 401 

