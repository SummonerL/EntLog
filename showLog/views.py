from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Entry

# Create your views here.
def index(request):
    order_by = request.GET.get('order_by', 'name')
    all_entries = Entry.objects.all().order_by(order_by)
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'all_entries': all_entries,
    })
    return HttpResponse(template.render(context))
