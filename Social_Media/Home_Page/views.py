from django.shortcuts import render
import mysql.connector
from .forms import user_cred


def home(request):
    return render(request,'home.html')

def login_signup(request):
    return render(request,'login_signup.html')

def register(request):
    if(request.method=='POST'):
        form = user_cred(request.POST)
        username = form.cleaned_data['last_name']
        print(username)
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="raviajay.2003",
      database="user_details"
)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM mytable")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


    return render(request,'login_signup.html')
