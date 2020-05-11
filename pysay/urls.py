from django.contrib import admin
from django.urls import path
from pysay import views

urlpatterns = [
	path('', views.index, name='home'),
	path('history/', views.history, name='history'),
    # path('admin/', admin.site.urls),
	]