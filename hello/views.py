# Create your views here.
from django.http import HttpResponse
from tropo import Tropo, Session
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

 
def hello(request):
  t = Tropo()
  msg = request.POST['msg']
  json = t.say("you just said: " + msg)
  json = t.RenderJson(json)
  return HttpResponse(json)