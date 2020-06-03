from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector

# Create your views here.
def login_form(request):
	return render(request,'login_page.html')

@csrf_exempt
def submit_form(request):
	username = request.POST.get('Username','')
	password = request.POST.get('Password','')
	print(username, password)

	if(username == 'admin' and password == 'secret'):
		mydb = mysql.connector.connect(host="localhost", user="root", 
								passwd="secretsecret",database="learn_python",
								auth_plugin="mysql_native_password")
		mycursor = mydb.cursor()
		mycursor.execute("select * from marks")
		rows =[]
		for row in mycursor:
			rows.append(row)
		print(rows)
		mydb.close();
		#return HttpResponse(rows[2])
		return HttpResponse("Welcome to Django Mr. %s. Here is DB data for you %s" % (username, rows[0]))
		#return render(request,'welcome.html')
	else:
		return HttpResponse("Invalid username and / or password %s" % username)
		#return render(request,'invalid.html')



