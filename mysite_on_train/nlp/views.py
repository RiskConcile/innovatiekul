from django.shortcuts import render
from .calcs import generate_image
# Create your views here.
from .models import InputMessage
from django.views.generic import CreateView , TemplateView

class InputMessageView(CreateView):
    model = InputMessage
    fields = ('client','text','upload_date')

class ProcessView(TemplateView):
    template_name = 'nlp/processed.html'
    model = InputMessage

    def get_context_data(self,**kwargs):
        context = super(ProcessView,self).get_context_data(**kwargs)
        context['raw_text'] = InputMessage.objects.get(id=kwargs['pk']).text
        context['image'] = generate_image(context['raw_text'])
        return context







