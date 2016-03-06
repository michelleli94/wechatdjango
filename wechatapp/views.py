from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import RequestContext

def index(request):
    return HttpResponse("Welcome to user management interface for Diamond in Rough")
    
def wechat(request):
    """Renders the wechat page."""
    assert isinstance(request, HttpRequest)
    fullurl = request.build_absolute_uri()
    wechatcode = request.GET.get('code', 'unknown')
    return render(
        request,
        'wechatapp/wechat.html',
        context_instance = RequestContext(request,
        {
            'fullurl':fullurl,
            'code':wechatcode,
            'message':'This is the original message',
        })
    )
