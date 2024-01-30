from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SearchForm


def search(request):
    # We have to handle the type of request GET/POST
    if request.method == "GET":
        # Create a form instance and populate it with request data
        form = SearchForm(request.GET)
        # check the validation of form
        if form.is_valid():
            # We have to validate the data here
            # Redirect to a new URL
            return HttpResponseRedirect("image")
    # If we receive any other form that POST we will return a blank form
    else:
        form = SearchForm()

    return render(request, "search_template.html", {"form": form})

