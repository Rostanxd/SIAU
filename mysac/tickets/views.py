from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Request

from .forms import RequestForm


def request_new(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            ticket_request = form.save()
            ticket_request.state = 'A'
            ticket_request.save()
            return redirect('tickets:request_detail', pk=ticket_request.pk)
    else:
        form = RequestForm()
    return render(request, 'tickets/request_edit.html', {'form': form})


def request_detail(request, pk):
    ticket_request = get_object_or_404(Request, pk=pk)
    return render(request, 'tickets/request_detail.html', {'request': ticket_request})


def request_edit(request, pk):
    ticket_request = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        form = RequestForm(request.POST, instance=ticket_request)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('tickets:request_detail', pk=post.pk)
    else:
        form = RequestForm(instance=ticket_request)
    return render(request, 'tickets/request_edit.html', {'request': ticket_request})


class ListRequestView(ListView):
    # model = Request
    template_name = 'tickets/requests_list.html'
    context_object_name = 'requests_list_all'

    def get_queryset(self):
        return Request.objects.all()


class DetailRequestView(DetailView):
    model = Request
    template_name = 'tickets/request_detail.html'

    def get_queryset(self):
        return Request.objects.all()


class CreateRequestView(CreateView):
    model = Request
    fields = '__all__'
    template_name = 'tickets/request_edit.html'

    def get_success_url(self):
        return reverse('requests-list')



