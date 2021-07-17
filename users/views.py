from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm

def register(request):
    """to register new user"""
    if request.method != 'POST':
        # Display a blank regstration form
        form = NewUserForm
    else:
        # Process completed form.
        form = NewUserForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            # Log in user and redirect to home page
            login(request, user)
            return redirect('tony_blogs:index')

    # Display a blank/invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)