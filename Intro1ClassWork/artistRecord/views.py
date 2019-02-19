from django.http import  HttpResponse

def badRoute(request):
    return HttpResponse("bad Route, use music.")

def index(resquest):
    return  HttpResponse(" artistOne , artistTwo , artistThree")

def artOne(request):
    return HttpResponse("something About this artist")

def artTwo(request):
    return  HttpResponse("Some strange fact i know")

def artThree(request):
    return  HttpResponse("A mysterious origin fact no one else knew")