from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """to register new user"""
    if request.method != 'POST':
        # Display a blank regstration form
        form = UserCreationForm
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log in user and redirect to home page
            login(request, new_user)
            return redirect('tony_blogs:index')

    # Display a blank/invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
