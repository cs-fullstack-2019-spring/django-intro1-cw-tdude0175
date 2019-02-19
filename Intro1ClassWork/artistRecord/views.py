from django.http import  HttpResponse

def index(resquest):
    return  HttpResponse("Bad Route. artistOne , artistTwo , artistThree")

def artOne(request):
    return HttpResponse("something About this artist")

def artTwo(request):
    return  HttpResponse("Some strange fact i know")

def artThree(request):
    return  HttpResponse("A mysterious origin fact no one else knew")