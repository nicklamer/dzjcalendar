# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from dzjcalendar.models import User

def index(request):
    return HttpResponse("Hello, world! You're at the dzjcalendar site.")

def calendar(request):
    user = User.objects.all()
    t = loader.get_template('calendar.html')
    c = Context({
        'users_list': user
        })
    return HttpResponse(t.render(c))

def calendar_frame(request):
    t = loader.get_template('calendar_frame.html')
    c = Context()
    return HttpResponse(t.render(c))
