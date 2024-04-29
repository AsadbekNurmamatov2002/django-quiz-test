from django.urls import path
from .views import *

app_name="quizes"

urlpatterns = [
    path("",quiz_list, name="quizlist"),
    path("<str:pk>/", quiz_datiel, name="quizsdatiel"),
    path("<str:pk>/data/", quiz_data_json, name="datajson"),
    path("<str:pk>/save/", save_quiz_data, name="datasave"),
    

]

