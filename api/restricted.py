from django.shortcuts import render


def restricted_urls(request):
    return render(request, 'api/users_list.html', {'approach': 1})