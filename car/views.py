from django.shortcuts import render,redirect
from .models import Members,Booking
# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def click_signup(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        mydata = Members.objects.filter(username=username).values()
        if not mydata:
            d = Members(username=username,password=password)
            d.save()
            return redirect('login')
        else:
            return redirect('login')
    return redirect('login')
def click_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mydata = Members.objects.filter(username=username,password=password).values()
        if mydata:
            return render(request,'dashboard.html',{'username':username})
        else:
            return redirect('signup')
    else:
        return redirect('login')

def dashboard(request):
    return render(request,'dashboard.html')

def book(request):
    username = request.POST['username']
    if request.method=='POST':
        service = request.POST['service']
        place = request.POST['place']
        
        d = Booking(service=service,place=place,approval='P',username=username)
        d.save()
    user = Members.objects.filter(username=username)
    book = Booking.objects.filter(username=username)
    return render(request,'profile.html',{'user':user,'book':book})

