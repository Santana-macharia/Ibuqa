from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import requests

def users_list(request):
    r = requests.get ('https://jsonplaceholder.typicode.com/users')
    data = r.json()
    return render(request, 'api/users_list.html', {'data': data})




