from django.shortcuts import render
from .forms import Students


# Create your views here.
def index(request):
    if request.method == 'POST':
        data = Students(request.POST)
        if data.is_valid():
            print("Form Validate")
            print("Username:" ,data.cleaned_data['Username'])
            print("Password:" ,data.cleaned_data['Password'])
    else:
        data = Students()
    return render(request ,'home.html' ,{'form': data})
