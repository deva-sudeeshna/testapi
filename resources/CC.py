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

class add_event(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('event_id',type=int,required=True,help="event_id cannot be left blank!")
        parser.add_argument("event_name",type=str,required=True,help="event_name cannot be left blank!")
        parser.add_argument('event_branch',type=str,required=True,help="event_branch cannot be left blank!")
        parser.add_argument('club_name',type=str,required=True,help="club_name cannot be left blank!")
        parser.add_argument('event_description',type=str,required=True,help="event_description cannot be left blank!")
        parser.add_argument('event_venue',type=str,required=True,help="user_id cannot be left blank!")
        parser.add_argument('event_loc',type=str,required=True,help="event_loc cannot be left blank!")
        data=parser.parse_args()

        try:
            x=query(f"""SELECT * FROM event_details where event_id = '{data["event_id"]}'""",return_json=False)
            if len(x)>0: 
                return {"message" : "Event already exists with this event_id!"},400
            else:
                query(f""" insert into event_details(event_id,event_name,event_branch,club_name,event_description,event_venue,event_loc) 
                            values({data['event_id']},'{data['event_name']}','{data['event_branch']}',
                                        '{data['club_name']}',
                                        '{data['event_description']}',
                                        '{data['event_venue']}',
                                        '{data['event_loc']}')""")
        except:
            return {"message" :"Error in details"},500
        return {"message":"Succesfully added event details"},201

class edit_event(Resource):
     def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('event_id',type=int,required=True,help="event_id cannot be left blank!")
        parser.add_argument("event_name",type=str,required=True,help="event_name cannot be left blank!")
        parser.add_argument('event_branch',type=str,required=True,help="event_branch cannot be left blank!")
        parser.add_argument('club_name',type=str,required=True,help="club_name cannot be left blank!")
        parser.add_argument('event_description',type=str,required=True,help="event_description cannot be left blank!")
        parser.add_argument('event_venue',type=str,required=True,help="user_id cannot be left blank!")
        parser.add_argument('event_loc',type=str,required=True,help="event_loc cannot be left blank!")
        data=parser.parse_args()

        try:
            x=query(f"""SELECT * FROM event_details where event_id = '{data["event_id"]}'""",return_json=False)
            if len(x)>0: 
                return {"message" : "Event already exists with this event_id!"},400
            else:
                query(f""" insert into event_details(event_id,event_name,event_branch,club_name,event_description,event_venue,event_loc) 
                            values({data['event_id']},'{data['event_name']}','{data['event_branch']}',
                                        '{data['club_name']}',
                                        '{data['event_description']}',
                                        '{data['event_venue']}',
                                        '{data['event_loc']}')""")
        except:
            return {"message" :"Error in details"},500
        return {"message":"Succesfully added event details"},201

class delete_event(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('event_id',type=int,required=True,help="event_id cannot be left blank!")
        data=parser.parse_args()
        try:
                x=query(f"""SELECT * FROM event_details where event_id = '{data["event_id"]}'""",return_json=False)
                if len(x)>0: 
                    query(f"""delete from event_details where event_id = '{data["event_id"]}'""",return_json=False)
                    return {"message" : "Event is Succesfully deleted!"},201
                else:
                    return{"message":"This Event_id doesn't exist!"},400
        except:
            return{"message":"Wrong details entered"},500





