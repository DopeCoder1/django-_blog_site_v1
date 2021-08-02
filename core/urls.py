from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
urlpatterns = [
    # path('', home_page, name='index'),
    # path('post/<slug:post_slug>/', post_details, name='posts'),
    # path('cats/<slug:cat_slug>/', show_category, name='categories'),
    # path('add_page/', addpage, name="addpage"),

    path('', HomeView.as_view(), name='index'),
    path('cats/<slug:cat_slug>/', CategoryView.as_view(), name='categories'),
    path('post/<slug:post_slug>/', PostView.as_view(), name='posts'),
    path('add_page/', AddPageView.as_view(), name='addpage'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser, name='logout'),
    path('contact/', ContactFormView.as_view(), name='contact')
]