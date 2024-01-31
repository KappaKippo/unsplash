import random

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render

from unsplash.settings import CLIENT_ID

from .forms import SearchForm


def search(request):
    # We have to handle the type of request GET/POST
    if request.method == "GET":
        # Create a form instance and populate it with request data
        form = SearchForm(request.GET)

        # check the validation of form
        if form.is_valid():
            # We have to validate the data here
            search_term = form.cleaned_data["user_search"]
            orientation = form.cleaned_data['orientation']
            color = form.cleaned_data['color']
            payload = {
                'client_id': CLIENT_ID,
                'query': search_term,
                'orientation': orientation if orientation else None,
                'color': color if color else None,
            }

            # Make the response to Unsplash
            response = requests.get('https://api.unsplash.com/search/photos/', stream=True, params=payload)

            # Get response data and select one random image to redirect to
            results = response.json().get('results')
            choice = random.choice(range(0, len(results)))
            image_url = results[choice].get('urls').get('raw')

            return HttpResponseRedirect(image_url)

    # If we receive any other form that POST we will return a blank form
    else:
        form = SearchForm()

    return render(request, "search_template.html", {"form": form})
