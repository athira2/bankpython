from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'new.html')
        else:

            messages.info(request,"Invalid credentials")
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

                user.save();
                return redirect('login')
                # print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")



def logout(request):
    auth.logout(request)
    return redirect('/')



def form(request):
    if request.method== 'POST':
        username = request.POST['username']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phonenumber = request.POST['phonenumber']
        email1 = request.POST['email1']
        address = request.POST['address']
        district = request.POST['district']
        branches = request.POST['branches']
        accounttype = request.POST['accounttype']
        materials = request.POST['materials']
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username taken")
            return redirect('register')
        elif User.objects.filter(email1=email1).exists():
            messages.info(request, "email taken")
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, dob=dob, age=age, gender=gender,
                                            phonenumber=phonenumber, email1=email1, address=address, district=district,
                                            branches=branches, accounttype=accounttype, materials=materials)

            user.save();
            return redirect('login')
            print("user created")



    return render(request,"form.html")
