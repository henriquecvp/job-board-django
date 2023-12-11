from django.urls import path
from .views import *

urlpatterns = [
    path('lista', job_list, name='job_list'),
    path('criar', create_job, name='job_create'),
    path('delete/<int:job_id>/', delete_job, name='delete_job'),
    path('edit/<int:job_id>/', edit_job, name='edit_job'),
    path('apply/<int:job_id>/', apply_for_job, name='apply_for_job'),
    path('<int:job_id>/', job_detail, name='job_detail'),
]