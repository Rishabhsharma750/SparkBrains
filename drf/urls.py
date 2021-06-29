from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.UserLoginView.as_view()),
    path('',include('api.urls'))
]
