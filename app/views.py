from django.shortcuts import render
from . models import *
# Create your views here.

'''
1. django forms
2. Creating custom page
3. 

Query :
ModelName.objects.create(
)

Fetch all the rows where product price is greater than 100


Product.objects.filter(
	price__gte =100
)


'''


def index_view(request):
	return render(request,'index.html')


def add_product_view(request):
	if request.method=='POST':
		product_name = request.POST.get('product_name')
		product_price = request.POST.get('product_price')
		product_quant = request.POST.get('product_quant')
		
		Product.objects.create(
			product_name=product_name,
			price = product_price,
			quantity = product_quant
		)
		return render(request,'add_product.html')

	else:
		return render(request,'add_product.html')

