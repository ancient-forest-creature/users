# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        print(f"save data is {data}")
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL('users_schema').query_db(query, data)
        return result

    @classmethod
    def get_user(cls, data):
        print(f"get_user data is {data}")
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL('users_schema').query_db(query,data)
        print(result)
        return cls(result[0])

    @classmethod
    def get_user_by_email(cls, data):
        print(f"get_user data is {data}")
        query = "SELECT * FROM users WHERE email=%(email)s;"
        result = connectToMySQL('users_schema').query_db(query,data)
        print(result)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def remove(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)