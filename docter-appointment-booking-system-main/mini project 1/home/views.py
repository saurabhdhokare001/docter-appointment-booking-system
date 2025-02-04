from django.shortcuts import render,HttpResponse
from home.models import Sign,Appointment
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password
# Create your views here.
def index(request):
    return render(request, 'home.html')
   #return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def docter(request):
    return render(request, 'docter.html')
    #return HttpResponse("this is services page")
    
def login(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        Email=request.POST.get("email")
        reemail=request.POST.get("cemail")
        city=request.POST.get("city")
        mobileno=request.POST.get("mob")
        password=request.POST.get("passwd")
        repassword=request.POST.get("cpasswd")

        if Email != reemail:
            return render(request, 'signup.html')
            messages.error(request, "Email is not match with previous email")
        if password != repassword:
            return render(request, 'signup.html')
            messages.error(request,'Password do not match with previous password.')

        signup = Sign(firstname=firstname,lastname=lastname,Email=Email,reemail=reemail,city=city,mobileno=mobileno,password=password,repassword=repassword)
        signup.save() 
    return render(request, 'login.html')
    #return HttpResponse("this is contact page")

def signup(request):
   
    return render(request, 'signup.html')

def log(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        Email = request.POST.get("email")
        reemail = request.POST.get("cemail")
        city = request.POST.get("city")
        mobileno = request.POST.get("mob")
        password = request.POST.get("passwd")
        repassword = request.POST.get("cpasswd")

        if Email != reemail:
            messages.error(request, "Email does not match the confirmation email")
            return render(request, 'signup.html')
        
        if password != repassword:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')

        # Save the password without hashing
        signup = Sign(
            firstname=firstname,
            lastname=lastname,
            Email=Email,
            reemail=reemail,
            city=city,
            mobileno=mobileno,
            password=password,  # Save plain text password
            repassword=repassword
        )
        signup.save()
        messages.success(request, "Signup successful!")
        return render(request, 'login.html')
    
    return render(request, 'login.html')

# Login view
def appoint(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            # Fetch the user based on the email
            user = Sign.objects.get(Email=username)

            # Directly compare the password
            if password == user.password:
                # Password matches, log the user in
                request.session['user_id'] = user.id  # Example of session handling
                return render(request, 'index.html')
            else:
                messages.error(request, "You entered an incorrect password.")
                return render(request, 'login.html')

        except Sign.DoesNotExist:
            # If the user with the provided email does not exist
            messages.error(request, "Invalid username")
            return render(request, 'login.html')

    return render(request, 'login.html')

def book(request):
    if request.method == "POST":
        username=request.POST.get("name")
        doctername=request.POST.get("docter")
        timeslot=request.POST.get("timeslot")
        appoint=Appointment (username=username,doctername=doctername,timeslot=timeslot)
        appoint.save()
        messages.success(request, "Appointment Book successful!")
        return render(request, 'index.html')