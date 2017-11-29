import unittest
from manage import app

class MongoTestCase(unittest.TestCase):
    
    mongodb_name = 'testing'
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        from mongoengine.connection import connect, disconnect, get_connection
        disconnect()
        connect(self.mongodb_name)
    
    def tearDown(self):
        from mongoengine.connection import get_connection, disconnect
        connection = get_connection()
        connection.drop_database(self.mongodb_name)
        disconnect()