from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    # return render(request, "home.html", {})
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            redirect('')
            all_items = List.objects.all()
            messages.success(request, ('Item has finally been added oooo'))
            return render(request, 'home.html', {'all_items': all_items, 'form':form,})
    else:
        messages.success(request, ('Form not Validated!'))
    all_items = List.objects.all()
    form = ListForm(request.POST or None)
    return render(request, 'home.html', {'all_items': all_items,'form':form,})
            