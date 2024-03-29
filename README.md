To start, in the terminal, enter:

    django-admin.py startproject mysite


This creates a directory that will have a few functions - manage the web server for development and 
direct the URL to the app.

To create the physical app, in the terminal, enter:

    python manage.py startapp hello

This will create another director. 

-----------------------------------------------------------------------------------------------------------------------

Files to change:

urls.py:


```py
from django.conf.urls.defaults import *
from hello.views import hello

urlpatterns = patterns('',
('^hello/$', hello)
)
```
What this really means -> ('^hello/$', hello)

`'^hello/$'` - This will be apart of the url to access the app.
example - http://www.yoursite.com/hello

```hello``` - This is the name of the method that will be called inside of view.py

-----------------------------------------------------------------------------------------------------------------------


hello/view.py:


```py
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
```
This is the app that gets runs. Notice that the method name is hello, the same as the method call in urls.py.

-----------------------------------------------------------------------------------------------------------------------

To start the development web-server, in the terminal (make sure that you are in the mysite directory), enter:
    
    python manage.pt runserver





  
