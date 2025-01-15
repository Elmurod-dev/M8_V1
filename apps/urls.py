from django.urls import path

from apps.views import HelleWorldAPIView, HelloNameAPIView, HelloLanguageAPIView, user_combo_view, user_post_combo_view, \
       motivation_view, helle_view, date_view

urlpatterns = [
       path('hello/',HelleWorldAPIView.as_view()),
       path('hello-name/',HelloNameAPIView.as_view()),
       path('hello-name-language/',HelloLanguageAPIView.as_view())
]


# Homework
urlpatterns+=[
       path('user/create/', user_combo_view),
       path('user/list/', user_combo_view),
       path('user/delete/<int:pk>', user_combo_view),
       path('user/update/<int:pk>', user_combo_view),
       path('post/update/<int:pk>/', user_post_combo_view),
       path('post/delete/<int:pk>', user_post_combo_view),
       path('post/create/', user_post_combo_view),
       path('post/list/', user_post_combo_view),
]

urlpatterns+=[
       path('get/motivation/',motivation_view),
       path('salom/',helle_view),
       path('get/date/',date_view),

]

