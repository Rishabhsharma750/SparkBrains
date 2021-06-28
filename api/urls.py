from django.urls import path
from api import views
from api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profile', UserProfileViewSet, basename='profile')
urlpatterns = router.urls

# urlpatterns = [
#     path('',views.url_list),
#     path('list/',views.student_list),
#     path('details/<int:num>/',views.student_details),
#     path('create/',views.student_create),
#     path('update/<int:num>/',views.student_update),
#     path('delete/<int:num>/',views.student_delete),
# ]