# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView ,DetailView
from django.shortcuts import get_object_or_404
from .models import Publisher, Book

class PublisherList(ListView):
    model = Publisher
    context_object_name = "my_favorite_publishers"
    def get_context_data(self, **kwargs):
        context = super(PublisherList, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context

class PublisherDetail(DetailView):
    model = Publisher
    def get_context_data(self, **kwargs):
        print(self.args, self.kwargs)
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context

class AcmeBookList(ListView):
    context_object_name = "book_list"
    queryset = Book.objects.filter(publisher__name= 'Acme Publishing')
    template_name = "books/acme_list.html"

class PublisherBookList(ListView):
    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        print(self.__dict__)
        # print self.kwargs
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)