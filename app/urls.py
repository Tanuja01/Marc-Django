from django.urls import path
from . import views

urlpatterns = [
	path('',views.index_view,name='index_view'),
	path('add/product/',views.add_product_view,name='add_product_view'),
	path('all/product/',views.all_product_view,name='all_product_view'),
	path('add/order/',views.add_order_view,name='add_order_view'),
	path('check/quant/',views.check_quant,name='check_quant'),
	path('edit/product/',views.edit_product,name='edit_product'),
]