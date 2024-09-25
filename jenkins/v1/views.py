from django.shortcuts import render
from django.http import request,JsonResponse

# Create your views here.

def main(request):
    return JsonResponse({'Message':'Hello World'})
