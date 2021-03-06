"""godjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from books.views import PublisherList, PublisherBookList, AuthorDetailView, RecordInterest, PublisherDetail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^publishers/<string:publisher>', PublisherList.as_view()),
    url(r'^publishers/(?P<pk>[0-9]+)', PublisherDetail.as_view()),
    # url(r'^publishers', PublisherList.as_view()),
    url('books/(?P<publisher>\w+)', PublisherBookList.as_view()),
    # url('^authors/(?P<pk>\d+)', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^author/(?P<pk>[0-9]+)/interest/$', RecordInterest.as_view(), name='author-interest')
]
