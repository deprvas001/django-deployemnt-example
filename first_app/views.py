from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
from . import forms
from first_app.forms import NewUserForm
from first_app.forms import UserForm, UserProfileInfoForm

#login
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def index1(request):
    my_dict = {'insert_me':'hello welcome back'}
    return render(request,'first_app/index.html',context=my_dict)

def topicList(request):
    topic_list = Webpage.objects.order_by('name')
    topics = {'topics_list': topic_list}
    return render(request, 'first_app/list.html',context=topics)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Do something code
            print("Validation success")
            print("Name: "+ form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print('Text: '+ form.cleaned_data['text'])
            
    return render(request, 'first_app/form_page.html', {'form':form})


def  users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')


    return render(request, 'first_app/users.html', {'form':form })


def relative(request):
    return render(request, 'first_app/relative.html')


def inheritance(request):
    return render(request, 'first_app/child.html')

def inheritanceFilter(request):
    context_dict = {'text':'hello World', 'number':100}
    return render(request, 'first_app/filterChild.html',context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html', {
        'user_form':user_form,'profile_form':profile_form,'registered':registered })

def user_login(request):

    if request.method == 'POST':
        # this key fetch from login.html for value
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active")

        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse('Invalid Login details')


    else:
        return render(request, 'first_app/login.html')  


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))   


@login_required
def special(request):
    return HttpResponse("You are logged In!")
