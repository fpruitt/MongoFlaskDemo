from application import db
from common.utilities import TimeUtils, DBFields

class User(db.Document):
    username = db.StringField(db_field=DBFields.username.value, required=True, unique=True)
    password = db.StringField(db_field=DBFields.password.value, required=True)
    email = db.EmailField(db_field=DBFields.email.value, required=True, unique=True)
    first_name = db.StringField(db_field=DBFields.first_name.value, max_length=75)
    last_name = db.StringField(db_field=DBFields.last_name.value, max_length=50)
    created = db.IntField(db_field=DBFields.created.value, default=TimeUtils.now())
    bio = db.StringField(db_field=DBFields.bio.value, max_length=50)
    
    meta = {
        'indexes': ['username', 'email', '-created']
    }