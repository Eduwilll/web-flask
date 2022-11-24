from flask import Blueprint, render_template, request, flash
from pymongo import MongoClient
import pdfkit

cluster = MongoClient("mongodb+srv://dbBot:admin@cluster0.yn32au7.mongodb.net/?retryWrites=true&w=majority") # endereço do mangodb
db = cluster["salgados"] #Banco de dados
admin = db["admin"] #Colletion user
users = db["users"]
complaint = db["complaint"]
orders = db["orders"]
chatbot = db["chatbot"]
auth = Blueprint('auth', __name__)


@auth.route("/teste", methods=['GET','POST'])
def teste():
    if request.method == 'POST':
        flash("Ralatório generado", category='success')

    #Usuarios
    a= []
    for x in users.find({}):
        #print(x)
        a.append(x)
    #complaints
    b = []
    for c in complaint.find({}):
        #print(c)
        b.append(c)
    #orders
    o = []
    for d in orders.find({}):
        #print(d)
        o.append(d)
    #nota
    n = []
    for f in chatbot.find({}):
        # print(d)
        n.append(f)
    return render_template("teste.html", value=a, comp=b, orders=o, nota=n)
@auth.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    return render_template('teste.html')

@auth.route("/login", methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route("/logout")
def logout():
    return "<h1>Logout</h1>"

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
    return render_template("sign_up.html")

