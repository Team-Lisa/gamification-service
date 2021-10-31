from mongoengine import connect, get_connection
import os
from api.Exceptions.empty_password_error import EmptyPasswordError



class DataBase():
    def __init__(self):
        db_name = os.environ.get('mode', 'test')
        if db_name == "test":
            connect('mongoenginetest', host='mongomock://localhost')
            conn = get_connection()
        else:
            if 'DB_PASSWORD' not in os.environ:
                raise EmptyPasswordError()
            db_password = os.environ['DB_PASSWORD']
            url = "mongodb+srv://lisa:{}@cluster0.9h1cn.mongodb.net/{}?retryWrites=true&w=majority".format(db_password,db_name)
            connect(host=url)