from django.contrib import admin
from django.urls import path
from adopcion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='lista_mascotas')
]
