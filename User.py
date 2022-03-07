from flask import jsonify


class User:
    def getAllUser():
        users = [
            {
                "id": 1, 
                "first_name": "a1", 
                "last_name": "a1", 
                "username": "a1"
            }, 
            {
                "id": 1, 
                "first_name": "a1", 
                "last_name": "a1", 
                "username": "a1"
            }, 
            {
                "id": 1, 
                "first_name": "a1", 
                "last_name": "a1", 
                "username": "a1"
            }, 
            {
                "id": 1, 
                "first_name": "a1", 
                "last_name": "a1", 
                "username": "a1"
            }, 
        ]
        return jsonify(users)