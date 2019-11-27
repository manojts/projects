from django.http import HttpResponse
from .models import item,truck,ware_house,procure_item,customer
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models import Q

def home(request):
	return render(request,'home.html')

def ware_house_login(request):
	if request.method == 'POST':
		w_place = request.POST['w_place']
		w_password=request.POST['w_password']

		single_ware = ware_house.objects.filter(ware_place=w_place).first()
		if single_ware == None:
			msg="The Ware-house location is invalid..!"
			back='ware_house_login'
			return render(request,'error.html',{'msg':msg,'back':back})
			
		else:
			if single_ware.ware_password == w_password:
				return redirect('ware_home',pk=single_ware.id)
			else:
				return render(request,'ware_login.html')
			

	return render(request,'ware_login.html')

def truck_login(request):
	if request.method == 'POST':
		t_number = request.POST['t_number']
		t_password=request.POST['t_password']

		single_truck = truck.objects.filter(truck_number=t_number).first()
		if single_truck == None:
			msg="The truck number is invalid..!"
			back='truck_login'
			return render(request,'error.html',{'msg':msg,'back':back})
			
		else:
			if single_truck.truck_password == t_password:
				return redirect('truck_home',pk=single_truck.id)
			else:
				return render(request,'truck_login.html')
			

	return render(request,'truck_login.html')

def ware_home(request,pk):
	single_ware = ware_house.objects.filter(id=pk).first()

	return render(request,'ware_home.html',{'single_ware':single_ware})
	
def truck_home(request,pk):
	single_truck = truck.objects.filter(id=pk).first()
	return render(request,'truck_home.html',{'single_truck':single_truck})
	
def procure_customer(request,pk_t):
	procure_item.objects.all().update(proc_quantity=0)
	procure_item.objects.all().update(proc_total_price=0)

	if request.method == 'POST':
		m_number = request.POST['m_number']
		c_name=request.POST['c_name']

		customer_single = customer.objects.filter(cust_number=m_number).first()
		if customer_single == None:
			new_cust=customer.objects.create(
					cust_number=m_number,
					cust_name=c_name)
					
			return redirect('procure_item_list',pk=new_cust.id,pk_t=pk_t)
			
		else:
			return redirect('procure_item_list',pk=customer_single.id,pk_t=pk_t)
			

	return render(request,'procure_cust.html',{'pk_t':pk_t})
	
def procure_item_list(request,pk,pk_t):
	# i_list = item.objects.all()
	v_list = procure_item.objects.all()
	
	if request.method == 'POST':
		i_id = request.POST['i_id']
		i_quantity = request.POST['i_unique']


		procure_item.objects.filter(id=i_id).update(proc_quantity=i_quantity)
		requiredis = procure_item.objects.filter(id=i_id).first()
		total = requiredis.proc_quantity * requiredis.proc_item_price
		procure_item.objects.filter(id=i_id).update(proc_total_price=total)

		
		return render(request,'procure_list.html',{'pk':pk,'v_list':v_list,'pk_t':pk_t})
	return render(request,'procure_list.html',{'pk':pk,'v_list':v_list,'pk_t':pk_t})
	
def ware_details(request,option,pk):
	if option == '1':
		w_t_list = truck.objects.filter(t_ware_id=pk)
		return render(request,'ware_list_truck.html',{'w_t_list':w_t_list,'pk':pk})
	if option == '2':
		w_i_list = item.objects.filter(i_ware_id=pk)
		return render(request,'ware_list_item.html',{'w_i_list':w_i_list,'pk':pk})
	if option == '3':
		cust = customer.objects.all()
		return render(request,'ware_list_cust.html',{'cust':cust,'pk':pk}) 
	

def billing(request,pk_c,pk_t):
	v_list = procure_item.objects.filter(~Q(proc_quantity=0))
	cust = customer.objects.filter(id=pk_c).first()
	total = procure_item.objects.all().aggregate(Sum('proc_total_price'))
	

	return render(request,'billing.html',{'v_list':v_list,'cust':cust,'total':total,'pk_t':pk_t})
	
def update_quantity_ware(request,pk_i,pk_w):
	single_item = item.objects.filter(id=pk_i).first()
	single_ware = ware_house.objects.filter(id=pk_w).first()
	if request.method == 'POST':
		
		item_quantity = request.POST['item_quantityf']


		item.objects.filter(id=pk_i).update(item_quantity_ware=item_quantity)
		
		
		return redirect('ware_details',option=2,pk=pk_w)
	return render(request,'update_quantity_ware.html',{'single_item':single_item,'single_ware':single_ware})



def selling_item_list(request,pk,pk_t,final_total):
	# i_list = item.objects.all()
	i_list = item.objects.all()
	
	
	cust=customer.objects.filter(id=pk).first
	
	if request.method == 'POST':
		i_id = request.POST['i_id']
		i_quantity = request.POST['i_unique']


		#procure_item.objects.filter(id=i_id).update(proc_quantity=i_quantity)
		requiredis = item.objects.filter(id=i_id).first()
		total = int(i_quantity) * requiredis.item_price
		final_total = int(final_total) + total
		
		

		return redirect('selling_item_list',pk=pk,pk_t=pk_t,final_total=final_total)		
	return render(request,'selling_item_list.html',{'i_list':i_list,'pk_t':pk_t,'cust':cust,'final_total':final_total})

def selling_customer(request,pk_t):
	final_total=0
	if request.method == 'POST':
		m_number = request.POST['m_number']
		c_name=request.POST['c_name']

		customer_single = customer.objects.filter(cust_number=m_number).first()
		if customer_single == None:
			new_cust=customer.objects.create(
					cust_number=m_number,
					cust_name=c_name)
					
			return redirect('selling_item_list',pk=new_cust.id,pk_t=pk_t,final_total=final_total)
			
		else:
			return redirect('selling_item_list',pk=customer_single.id,pk_t=pk_t,final_total=final_total)
			

	return render(request,'procure_cust.html',{'pk_t':pk_t})

def sell_billing(request,pk_t,pk_c,tot):
	cust = customer.objects.filter(id=pk_c).first()
	truc = truck.objects.filter(id=pk_t).first()
	return render(request,'sell_billing.html',{'truc':truc,'cust':cust,'tot':tot,'pk_t':pk_t})

def truck_items(request,pk_t):
	items= item.objects.filter(i_truck_id=pk_t)
	return render(request,'truck_items.html',{'items':items,'pk_t':pk_t})
