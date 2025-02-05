from django.urls import path, re_path
from women import views
from women.views import page_not_found

urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
    re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),
]



