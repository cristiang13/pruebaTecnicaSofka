from . import views
from django.urls import include, path

urlpatterns = [
     path('', views.home),
     path('add_nave', views.add_nave, name="add_nave"),
     path('store_nave', views.store_nave, name="store_nave"),
     path('search_nave', views.search, name='search_nave'),
     path('get_naves',views.get_naves, name="get_naves")
     
]