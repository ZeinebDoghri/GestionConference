from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
from django.contrib.auth import logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Handle registration logic here
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form}) # the goal of render is to return an HttpResponse object with the rendered template

def logout_view(request):
    logout(request)
    return redirect('login')