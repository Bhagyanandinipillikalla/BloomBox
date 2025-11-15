from django.shortcuts import render,redirect
from .models import Plant
from django.contrib.auth import authenticate
from .forms import PlantForm,AccountForm,LoginForm

# Create your views here.


def plant_list(request):
    plants = Plant.objects.all()
    return render(request, "plant_list.html", {"plants": plants})

def plant_detail(request, id):
    plant = Plant.objects.get(id=id)
    return render(request, "plant_detail.html", {"plant": plant})

def plant_insert(request):
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("app1:plant_list")
    else:
        form = PlantForm()
    return render(request, "form.html", {"form": form})

def plant_update(request, id):
    plant = Plant.objects.get(id=id)
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("app1:plant_list")
    else:
        form = PlantForm()
    return render(request, "form.html", {"form": form})


def plant_delete(request, id):
    plant = Plant.objects.get(id=id)
    if request.method == "POST":
        plant.delete()
        return redirect("app1:plant_list")  
    return render(request, "delete.html", {"plant": plant})



def register(request):
    if request.method=='POST':
        form=AccountForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("app1:login_user")
    else:
        form=AccountForm()
    return render(request,'create.html',{'form':form})


    
def login_user(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(username=username,password=password)
            if user is not None:
                return redirect("app1:plant_list")
            else:    
                form.add_error(None,"Invalid username or password")
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})    
