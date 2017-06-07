from  peewee import *

from  os import path
ROOT= path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(ROOT,"apis.db"))

class User(Model):
    names= CharField()
    email= CharField(unique=True)
    age = IntegerField()
    class Meta:
        database = db

# User.create_table()
# User.create(names="Tom Juma", email="tom@yahoo.com", age =18)
# User.create(names="Sam Terry", email="sam@yahoo.com", age =23)
# User.create(names="Hellen Jane", email="hellen@yahoo.com", age =34)
# User.create(names="Thomas Edison", email="eddy@yahoo.com", age =77)