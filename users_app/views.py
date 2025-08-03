from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from users_app.forms import CustomRegisterForm
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'New User Account Created, Login to Continue!')
            return redirect('register')  # or redirect to 'login'
        else:
            # ❗ Form is invalid: fall through to re-render the page with form + errors
            messages.error(request, 'Registration failed. Provide correct details.')
            return render(request, 'register.html', {'register_form': register_form})
    
    else:
        register_form = CustomRegisterForm()
        return render(request, 'register.html', {'register_form': register_form})



def test_logout(request):
    logout(request)
    return render(request,'logout.html')