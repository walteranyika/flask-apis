from flask import Flask, jsonify, request
from  users_model import  User
from peewee import IntegrityError
app = Flask(__name__)


@app.route('/all', methods=["GET"])
def all():
    users = User.select()
    users_list=[]
    for item in users:
       users_list.append({"id":item.id, "names":item.names, "email":item.email,"age":item.age})
    return jsonify(users_list)

@app.route("/user/<int:id>", methods=["GET"])
def fetch_user(id):
    try:
      item = User.get(User.id == id)
      return  jsonify({"id":item.id, "names":item.names, "email":item.email,"age":item.age})
    except User.DoesNotExist:
      return jsonify({"response": "User does not exists"})


@app.route("/save", methods=["POST"])
def save():
    if request.method == 'POST':
        names = request.form["names"]
        email = request.form["email"]
        age = request.form["age"]
        try:
            User.create(names=names, email=email, age=age)
            return jsonify({"response":"Saved"})
        except IntegrityError:
            return jsonify({"response":"User already exists"})
    else:
        return jsonify({"response": "No data was sent"})

#http://127.0.0.1:5000/update/1
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    if request.method == 'POST':
        names = request.form["names"]
        email = request.form["email"]
        age = request.form["age"]
        try:
            user = User.get(User.id == id)
            user.names= names
            user.email= email
            user.age = age
            user.save()
            return jsonify({"response":"Updated Successfully"})
        except User.DoesNotExist:
            return jsonify({"response": "User Does Not Exist"})
    else:
        return jsonify({"response":"Wrong Request"})


@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    if request.method == 'DELETE':
        try:
            user = User.get(User.id == id)
            user.delete_instance()
            return jsonify({"response": "Deleted Successfully"})
        except User.DoesNotExist:
            return jsonify({"response": "User Does Not Exist"})
    else:
        return jsonify({"response": "Failed To Delete"})



# if __name__ == '__main__':
#     app.run()



#save
#fetch all
#fetch one
#delete
#update
#pythonanywhere






