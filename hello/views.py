# Create your views here.
#sends information back to Tropo
from django.http import HttpResponse  
#This will allow you to call Tropo functions
from tropo import Tropo 
#This will bypass authorization
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

 
# hello is the method name called by urls.py 
def hello(request): 
  t = Tropo()
  #This is the initial text that you want
  msg = request.POST['msg'] 
  #This sends a text reply back
  json = t.say("you just said: " + msg) 
  #This renders the reply into JSON so Tropo can read it
  json = t.RenderJson(json) 
  #This sends the JSON to Tropo
  return HttpResponse(json) 