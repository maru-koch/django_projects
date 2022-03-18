from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly = {
        'january': 'January Challenge',
        'february': 'February Challenge',
        'march': 'March Challenge',
        'april': 'April Challenge',
        'may': 'May Challenge',
    }
month_list = monthly.keys()

#: 7
#: adding an index page for the challenge app --> /challenge/

def index(request):
    #: to collect all the list items for each month into a string
    list_items = ""
    for month in month_list:
        #: construct a url_path for each month using the reverse method
        #: challenge/january
        #: where challenge is the url of the app and january is the end point(args = january)

        url_path = reverse("monthly_challenge", args = [month])

        capitalized_month = month.capitalize()
        list_items += f"<li><a href = '{url_path}'>{capitalized_month}</a></li>"
    
    template = f"""<ul>{list_items}</ul>"""
    return HttpResponse(template)

def monthly_challenge(request, month):
    if month in month_list:
        # return HttpResponse(monthly[month])

        # STEP 6

        # it is unrealistic to return a test as a response
        # so we are going to use some html elements instead
        # we will inject the test in the html elements

        template = f"<h1>{monthly[month]}</h1>"

        return HttpResponse(template)

    return HttpResponseNotFound(f"{month} is not supported")


def monthly_challenge_by_number(request, month):
    months = list(month_list)
    month = months[month -1]
    
    # return HttpResponseRedirect("/challenges/" + month)

    #: STEP 5

    # it is bad practice to hard code a path as used in the HttpResponseRedirect above
    # instead, use the reverse() to dynamically construct the paths
    # to use the reverse function, u need to name your url in the 
    # path method in the list of urlpatterns in url.py
    # import reverse from django.url

    url_path = reverse("monthly_challenge", args = [month])
    return HttpResponseRedirect(url_path)

    # whenever you redirecting a url, consider using the reverse funtion and 
    # naming your url


