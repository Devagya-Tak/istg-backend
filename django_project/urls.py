from django.contrib import admin
from django.urls import path
from home.views import login, post_question, get_questions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('post/<int:pk>/', post_question),
    path('get/<int:pk>/', get_questions)
]
