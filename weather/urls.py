
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('weather_result/', views.weather_result, name='weather_result'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
    # path('social_links', views.social_links),
]
