from django.http import request
from django.http.response import HttpResponse

from django.shortcuts import render
from my_app.forms import UserForms,UserProfileInfoForm


# for login logout
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect ,HttpRequest
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'my_app/index.html')

# logout only if user login
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))




def register(request):
    registered =False

    if request.method == 'POST':                               # if form is post

        user_form = UserForms(data= request.POST)              # grabe the information from userform 
        profile_form = UserProfileInfoForm(data =request.POST) # # grabe the information from userProfileInfoForm


        if user_form.is_valid() and profile_form.is_valid():         # if form is valid or not (means apllied information is in correct order or not)
            
            user = user_form.save()               #  save information into database
            user.set_password(user.password)      # convert password into hash value from goes to settings,py 
            user.save()                                # no finally save user into database
            

            profile =profile_form.save(commit=False)       # we dont save the profile_form other wise we get error collision occor
                                                            # above error collision is beacuse override from user  from where we specify onetoone relationship we use 

            profile.user =user                       # profile.user m user  user = models.OneToOneField(User,on_delete=models.CASCADE) h 
                                                    # and right side vale user m user , user = user_form.save()  h

            if 'profile_pic' in request.FILES :
                profile.profile_pic = request.FILES['profile_pic']   # profile dectionary where files uploaded
                                                                       # ['profile_pic'] key name is similer to name define in modeles


            profile.save()                                # save into data base
            
            registered = True
        
            
        else:
            print("someone summit invalid form")
            print(user_form.errors,profile_form.errors)
    


    else:

        user_form =UserForms()
        profile_form = UserProfileInfoForm()

    return render(request,'my_app/registration.html',{'user_form':user_form,
                                                          'profile_form':profile_form,
                                                           'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username =request.POST.get('username')   # .get method is used to get username from login form 
                                                 # here .get('username') is  name="username"  in login.html page
        password = request.POST.get('password')
        
        user = authenticate(username = username , password = password)    # this function return an object if username and password match in database
                                                                         # if login username or password does not match to data base then it return none
        

        if user:               # if user !=  none 

            if user.is_active:                          # if user is on login site and fill correct information and its account active
                login(request,user)                     #  login the uuser
                return HttpResponseRedirect(reverse(index))   # return user to index.html page

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE !")

        else:
            print("some non registred try to login ")
            print("username: {} password : {} ".format(username,password))

            return HttpResponse("Account not registered ")
    

    return render(request, 'my_app/login.html',{})

    














 

