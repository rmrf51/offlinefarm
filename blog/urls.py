from django.urls import path
from .views import BlogListView,BlogDetailView, BlogAbout, BlogApp, BlogPrice, BlogContacts, BlogDelivery

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('about/', BlogAbout.as_view(), name='about'),
    path('app/', BlogApp.as_view(), name='app'),
    path('price/', BlogPrice.as_view(), name='price'),
    path('contacts/', BlogContacts.as_view(), name='contacts'),
    path('delivery/', BlogDelivery.as_view(), name='delivery'),
]
