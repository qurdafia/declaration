from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SubForm
from django.contrib import messages



# Registering a guest
def register_guest(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            # cleaned = form.cleaned_data
            form.save()
            messages.success(request, 'Guest is registered successfully!')
            return redirect('thank_you')
    else:
        form = SubForm()

    return render(request, 'register_guest.html', {'form': form})


def thank_you(request):
    return render(request, 'thank_you.html')
