from django.contrib import admin
from django.urls import path
from analysis.views import cngm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cngm/', cngm)
]
