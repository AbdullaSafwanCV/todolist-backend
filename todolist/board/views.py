from django.shortcuts import render , redirect
from .models import AddNote


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)  # redirect to homepage or dashboard
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, "register.html")  # uses same form page

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect(login_view)

    return render(request, "register.html")  # same template handles both
       
def logout_view(request):
    logout(request)
    return redirect(login_view)

@login_required(login_url="login")
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        duedate = request.POST.get('duedate')
        AddNote.objects.create(title=title, content=content, duedate=duedate, user=request.user)
        return redirect('index')
    addcard = AddNote.objects.filter(completed=False, user=request.user)
    completed_cards = AddNote.objects.filter(completed=True, user=request.user)
    return render(request, 'index.html', {"AddCard": addcard, "completed_cards": completed_cards})

def completed(request, id):
    card = AddNote.objects.get(id=id)
    card.completed = not card.completed 
    card.save() 
    return redirect('index')

def delete(request, id):
    card = AddNote.objects.get(id=id)
    card.delete()
    return redirect('index')

def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        duedate = request.POST.get('duedate')
        print("++++++++++", request.user)
        AddNote.objects.create(title=title, content=content, duedate=duedate, user=request.user)
        return redirect('index')
    return render(request, 'index.html')

