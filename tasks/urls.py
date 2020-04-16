from django.urls import path
from . import views
urlpatterns = [
	path('',views.user_order_page),
	path('thanks/',views.thanks, name='list'),
	path('kitchen/',views.index, name='kitchen'),
	path('delete/<str:pk>/',views.deleteTask, name ='delete'),
	path('confirm/<str:pk>/',views.confirmTask, name ='confirm')
]