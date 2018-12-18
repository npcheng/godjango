# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin

from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Publisher, Book, Author


class PublisherList(ListView):
    model = Publisher
    context_object_name = "my_favorite_publishers"

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name = self.kwargs['publisher'])
        print "fy"
        print(self.kwargs)
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # context = super(PublisherList, self).get_context_data(**kwargs)
        context = super(PublisherList, self).get_context_data(**kwargs)

        context['publisher'] = self.publisher
        return context


# class PublisherDetail(DetailView):
#     model = Publisher

    # def get_context_data(self, **kwargs):
    #     print(self.args, self.kwargs)
    #     context = super(PublisherDetail, self).get_context_data(**kwargs)
    #     context['book_list'] = Book.objects.all()
    #     return context


class PublisherDetail(SingleObjectMixin, ListView):
    paginate_by = 2
    template_name = "books/publisher_detail.html"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Publisher.objects.all())
        print self.object
        return super(PublisherDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PublisherDetail,self).get_context_data(**kwargs)
        context["publisher"] = self.object
        return context

    def get_queryset(self):
        return self.object.book_set.all()

class AcmeBookList(ListView):
    context_object_name = "book_list"
    queryset = Book.objects.filter(publisher__name='Acme Publishing')
    template_name = "books/acme_list.html"


class PublisherBookList(ListView):

    template_name = 'books/books_by_publisher.html'
    context_object_name = 'my_favorite_publishers'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super( PublisherBookList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher

        print(context)
        return context

class AuthorDetailView(DetailView):

    queryset = Author.objects.all()

    def get_object(self):
        print "xxx"
        obj = super(AuthorDetailView, self).get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj

class RecordInterest(SingleObjectMixin, View):
    """Records the current user's interest in an author."""
    model = Author

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # Look up the author we're interested in.
        self.object = self.get_object()
        print self.object
        # Actually record interest somehow here!

        return HttpResponseRedirect(reverse('author-detail', kwargs={'pk': self.object.pk}))
