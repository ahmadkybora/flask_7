from flask import Flask, jsonify, render_template, request, template_rendered, abort
import os
from User import User
app = Flask(__name__)

# # یک مسیر مشخص
# path = os.path.join("uplods")
# # مسیر بالا را میسازد تابع زیر
# os.makedirs(path)

@app.errorhandler(404)
def showError(err):
    return err
@app.route("/")
def index():
    # return abort(404)
    # name = [
    #     {
    #         "id": 1, 
    #         "first_name": "a1", 
    #         "last_name": "a1", 
    #         "username": "a1"
    #     }, 
    #     {
    #         "id": 1, 
    #         "first_name": "a1", 
    #         "last_name": "a1", 
    #         "username": "a1"
    #     }, 
    #     {
    #         "id": 1, 
    #         "first_name": "a1", 
    #         "last_name": "a1", 
    #         "username": "a1"
    #     }, 
    #     {
    #         "id": 1, 
    #         "first_name": "a1", 
    #         "last_name": "a1", 
    #         "username": "a1"
    #     }, 
    # ]
    # user = User(__name__)
    # requestAll = request.args.get('name', 'id')
    # id = request.args['id']
    # return id
    # user = User()
    # return user.getAllUser
    # return jsonify(name)
    return render_template("index.html")

@app.route("/user/store", methods=["POST"])
def ab():
    id = request.form['username']
    file = request.files['file']
    return id
    # if file.filename != "":
    #     try:
    #         # فایل زیر را در آدرس مورد نظر ذخیره میکند
    #         file.save(os.path.join(path, file.filename))
    #     except Exception as e:
    #         return "asd"
    # else:
    #     return id
# @app.route("/a/<int:name>")
# def get(name):
#     if name is 2:
#         return "go"
#     # ali = [
#     #     {
#     #         "is": "go", 
#     #         "a": "l"
#     #     }
#     # ]
#     return render_template("index.html", name)

# validation file
fileName = "a.pp"
fileName2 = "ab.py"
def validFile(fileName):
    ff = fileName.rsplit(".", 1)[1]
    return "." in fileName and ff
app.run(debug=True)
