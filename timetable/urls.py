from django.urls import path
from . import views


app_name="timetable"
urlpatterns = [
    path('',views.index, name='index'),
    path('qualification',views.list_qualification, name='qualification'),
    path('timetable/<str:national_code>',views.timetable, name='timetable'),

]