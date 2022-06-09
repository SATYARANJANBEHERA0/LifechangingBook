from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class BookListView(ListView):
    model = Book
class BookDetailView(DetailView):
    model = Book
class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('homepage')
