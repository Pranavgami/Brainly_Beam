from django.shortcuts import render,redirect
from django.shortcuts import redirect
from .models import Form
import csv
# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        user=request.POST['user']
        password=request.POST['pass']
        form = Form(username=user,password=password)
        form.save()
        
        file = open('File.csv',mode='a',newline='')
        writer = csv.writer(file)
        
        if file.tell() == 0:
            writer.writerow(['Username','Password'])
        writer.writerow([user,password])
        file.close()
        return redirect('home')
        
    return render(request,'signup.html')
        