from flask import Blueprint, render_template, request, flash
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://dbBot:admin@cluster0.yn32au7.mongodb.net/?retryWrites=true&w=majority") # endereço do mangodb
db = cluster["salgados"] #Banco de dados
admin = db["admin"] #Colletion user
auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route("/logout")
def logout():
    admin1 = admin.find_one()
    return f"<h1>Logout{admin1}</h1>"

@auth.route("/sign-up", methods=['GET','POST'])
def signup():
    online_users = cluster.db.users.find({"online": True})
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Digite um E-mail valido!', category='error')
        elif len(firstname) < 2:
            flash('Digite um E-mail valido!', category='error')
        elif password2 != password1:
            flash('A senha digitada é diferente!', category='error')
        elif len(password1) < 7:
            flash('Digite uma senha com pelo meno 8 caracteres', category='error')
        else:
            # add user to database
            flash("Conta criada", category='success')
            users.insert_one({"number": number, "ProfileName": profileName, "channel": "whatsapp", "status": "main", "messages": []})
    return render_template("sign_up.html")

