from django.contrib import admin
from django.urls import path
from comics import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # Otros paths según sea necesario
]
