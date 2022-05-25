from django.shortcuts import render

from logs.forms import WhatForm
from .models import Whatsapp
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

# Create your views here.
def HomePage(request):
    form = WhatForm
    if request.method == 'POST':
        form = WhatForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'base.html', context)

class PostDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "Post/detail.html"
    model = Whatsapp
    context_object_name = "post"



class CreateNewPost(CreateView):
    model = Whatsapp
    template_name = "Post/create.html"
    fields = ('__all__')
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super().form_valid(form)

 