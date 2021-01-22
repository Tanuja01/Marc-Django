from django.shortcuts import render,redirect
from . models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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

def all_product_view(request):
	products = Product.objects.all()
	return render(request,'all_product.html',{'products':products})

def add_product_view(request):
	if request.method=='POST':
		product_name = request.POST.get('product_name')
		product_price = request.POST.get('product_price')
		product_quant = request.POST.get('product_quant')
		
		if product_name=='':
			return render(request,'add_product.html',{'message':'Product Name cannot be blank'})

		Product.objects.create(
			product_name=product_name,
			price = product_price,
			quantity = product_quant
		)
		return render(request,'add_product.html')

	else:
		return render(request,'add_product.html')



def add_order_view(request):
	if request.method=='POST':
		prod_id = request.POST.get('prod_id')
		purchase_quant = int(request.POST.get('purchase_quant'))
		prod = Product.objects.filter(id=prod_id)
		if prod:
			avail_quant = prod[0].quantity-purchase_quant
			prod.update(quantity=avail_quant)

			Order.objects.create(
				product=prod[0],
				quantity_purchased = purchase_quant)
			return redirect('all_product_view')
	else:
		product_id = request.GET.get('id')	
		product = Product.objects.filter(id=product_id)
		print(product)
		if product:
			return render(request,'add_order.html',{'product':product[0]})
		else:
			return redirect('all_product_view')

@csrf_exempt
def check_quant(request):
	input_quant = request.POST.get('input_quant')
	produc_id = request.POST.get('produc_id')

	#to check whether any product of that id exists or not
	product = Product.objects.filter(id=produc_id,quantity__gte=input_quant) 
	if not product:
		return JsonResponse({'status':'Error error occured. Check your quantity'})

	else:
		return JsonResponse({'status':'success'})


@csrf_exempt
def edit_product(request):
	name =request.POST.get('name')
	quant =request.POST.get('quant')
	price =request.POST.get('price')
	edit_id =request.POST.get('edit_id')

	Product.objects.filter(id=edit_id).update(
		price =price,
		quantity=quant
		)

	return JsonResponse({'status':'success'})