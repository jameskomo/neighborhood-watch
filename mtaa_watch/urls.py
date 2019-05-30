from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    NeighborhoodListView,
    NeighborhoodDetailView,
    NeighborhoodCreateView,
    NeighborhoodUpdateView,
    NeighborhoodDeleteView,
    BusinessListView,
    BusinessDetailView,
    BusinessCreateView,
    BusinessUpdateView,
    BusinessDeleteView,
    ContactListView,
    ContactDetailView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView,
    
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='mtaa_watch-home'),
    path('business/', BusinessListView.as_view(), name='business-home'),
    path('neighborhood/', NeighborhoodListView.as_view(), name='neighborhood-home'),
    path('contact/', BusinessListView.as_view(), name='contact-home'),
    # DETAIL VIEWS
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('neighborhood/<int:pk>/', NeighborhoodDetailView.as_view(), name='neighborhood-detail'),
    path('business/<int:pk>/', BusinessDetailView.as_view(), name='business-detail'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    # CREATE VIEWS
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('neighborhood/new/', NeighborhoodCreateView.as_view(), name='neighborhood-create'),
    path('business/new/', BusinessCreateView.as_view(), name='business-create'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    # UPDATE VIEWS
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('neighborhood/<int:pk>/update/', NeighborhoodUpdateView.as_view(), name='neighborhood-update'),
    path('business/<int:pk>/update/', BusinessUpdateView.as_view(), name='business-update'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    # DELETE VIEWS
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('neighborhood/<int:pk>/delete/', NeighborhoodDeleteView.as_view(), name='neighborhood-delete'),
    path('business/<int:pk>/delete/', BusinessDeleteView.as_view(), name='businesss-delete'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
    path('about/', views.about, name='mtaa_watch-about'),
]
