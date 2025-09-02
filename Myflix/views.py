from django.http import JsonResponse
from django.shortcuts import render

def users(request):
    if request.method == 'GET':
        user={
            'id':1,
            'nome': 'josé'
        }
        return JsonResponse(user)


