from django.conf.urls import url

from art import views, search_handler, detail_handler
from art.views import add_handler

urlpatterns = [
    url(r'^index/', views.IndexHandler),
    url(r'^search/', search_handler.SearchHandler),
    url(r'^detail/', detail_handler.Detail_handler),
    url(r'^add', add_handler),
]
