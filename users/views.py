from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm  # to add another field so we imported from forms.py
# Create your views here.


def register(request):
    if request.method == "POST":  # if we get a post request
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created!! ')
            return redirect('login')

    else:
        form = UserRegisterForm()  # else just an empty form get request
    return render(request, 'users/register.html', {'form': form})


@ login_required()
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid:
            u_form.save()
            messages.success(request, 'Your info has been updated!! ')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'users/profile.html', context)
