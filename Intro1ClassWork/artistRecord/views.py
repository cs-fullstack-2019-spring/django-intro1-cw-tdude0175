from django.http import  HttpResponse

# you could run through a list possibly to give one of the three artists

# used for default routing
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


# YOU CAN ROUTE THROUGH EMPTY INPUT FOR OVERRIDING DEFAULT FIRST!!