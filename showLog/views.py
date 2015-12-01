from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.template import RequestContext, loader

from .models import Entry
from .models import EntryForm

# Create your views here.
def index(request):
    order_by = request.GET.get('order_by', 'name')
    filter_type = request.GET.get('filter', '')
    if filter_type:
        all_entries = Entry.objects.filter(ent_type=filter_type).order_by(order_by)
    else:
        all_entries = Entry.objects.all().order_by(order_by)
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'all_entries': all_entries,
    })
    return HttpResponse(template.render(context))

def add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('..')
    else:
        form = EntryForm()
    return render(request, 'add_entry.html', {'form': form})
