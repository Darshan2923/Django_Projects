from django.shortcuts import render,HttpResponse
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
def index(request):
    context={}
    return render(request,'ecomapp/index.html',context)

def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems=order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0,'shipping':False}
		cartItems=order['get_cart_items']

	context = {'items':items, 'order':order,'cartItems':cartItems}
	return render(request, 'ecomapp/cart.html', context)

def store(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems=order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0,'shipping':False}
		cartItems=order['get_cart_items']
	
	products=Product.objects.all()
	context={'products':products,'order':order,'items':items,'cartItems':cartItems}
	return render(request,'ecomapp/store.html',context)


def checkout(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems=order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0,'shipping':False}
		cartItems=order['get_cart_items']

	context = {'items':items, 'order':order,'cartItems':cartItems}
	return render(request, 'ecomapp/checkout.html', context)



def updateItem(request):
	data=json.loads(request.body)
	productId=data['productId']
	action=data['action']
	print('Action: ',action)
	print('productId: ',productId)

	customer=request.user.customer
	product=Product.objects.get(id=productId)
	order,created=Order.objects.get_or_create(customer=customer,complete=False)
	orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)

	if action=='add':
		orderItem.quantity=(orderItem.quantity+1)
	if action=='remove':
		orderItem.quantity=(orderItem.quantity-1)

	orderItem.save()

	if orderItem.quantity<=0:
		orderItem.delete()
	return JsonResponse('Item was added',safe=False)
    
    
