from django.urls import path
from .views import *

urlpatterns = [
    # path('', home_page, name='index'),
    # path('post/<slug:post_slug>/', post_details, name='posts'),
    # path('cats/<slug:cat_slug>/', show_category, name='categories'),
    # path('add_page/', addpage, name="addpage"),

    path('', HomeView.as_view(), name='index'),
    path('cats/<slug:cat_slug>/', CategoryView.as_view(), name='categories'),
    path('post/<slug:post_slug>/', PostView.as_view(), name='posts'),
    path('add_page/', AddPageView.as_view(), name="addpage"),
]