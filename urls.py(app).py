Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from django.urls import path
... from . import views
... 
... urlpatterns = [
...     path('', views.index, name='home'),
...     path('create/', views.create_profile, name='create'),
...     path('hospital_login/', views.hospital_login, name='hospital_login'),
...     path('access/', views.hospital_access, name='access'),
