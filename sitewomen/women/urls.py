from django.urls import path, re_path
from women import views
from women.views import page_not_found

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive, name='archive'),
]



