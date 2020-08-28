from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return HttpResponse("<h1>hi welcome to django sescition</h1>")
def index(request):
    return HttpResponse("<h4>Hi<mark>KAMALESH</mark>welcome to django sescition</h4>")
def hello(request,name,roll):
    return HttpResponse("<h2> hi my name is:{} <br>Your rollnumber is: {} </h2>".format(name,str(roll)))
def message(request):
    return render(request,'myApp/message.html',{})
def details(request):
    data = {'name': 'kamal',"rollno": 1424}
    return render(request,'myApp/details.html',{'data':data})
def register(request):
    if request.method == "POST":
        name = request.POST["uname"]
        mobile = request.POST['mbno']
        email = request.POST['email']
        print(name,mobile,email)
        return HttpResponse("your record is added successfully")
    return render(request,'myApp/register.html',{})
def table(request,num):
    table = num
    number = [num+1 for num in range(11)]
    result = [table*i for i in number]
    mylist = zip(number, result)
    return render(request,'myApp/table.html',{'mylist': mylist, 'table': table})
