from django.shortcuts import render
import pyodbc

def home(request):
    return render(request,'home.html')

def login_signup(request):
    return render(request,'login_signup.html')

def register(request):
    server_name = 'DESKTOP-R3D7KGJ'
    database_name = 'user_details'
    username = 'root'
    password = 'raviajay.2003'

    connection_string = f"Driver={{SQL Server}};Server={server_name};Database={database_name};UID={username};PWD={password}"
    cnxn = pyodbc.connect(connection_string)
    print(cnxn)
    return render(request,'login_signup.html')
