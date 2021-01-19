from django.urls import path
from . import views

urlpatterns = [
	path('',views.index_view,name='index_view'),
	path('add/product/',views.add_product_view,name='add_product_view'),
]