
from django.http import HttpResponse
from .models import dept_master,sub_dept,tender,bidding,company,complaint
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.models import User


def home(request):
	dept_names= dept_master.objects.all()
	tender_names= tender.objects.all()
	compl = complaint.objects.all()
	return render(request,'home.html',	{'dept_names':dept_names,'tender_names':tender_names,'compl':compl})
#it is link which sends the objects of dept,tender,complaint to the home page for rendering


def requesting(request,user_data):
	if request.method == 'POST':
		company_reg_no = request.POST['company_reg_no']		
		topic = company.objects.create(
			c_name = user_data,
			c_reg_no = company_reg_no
			)
		return redirect('home')
	return render(request,'requesting.html')
# This renders the page requesting the company to give company registration number
#and gets the currently logged in user name and creates a company object.


def sub_departments(request, pk):
	
	sub_depts=sub_dept.objects.filter(D_Id=pk)
	dept_name = dept_master.objects.filter(id=pk)
	dept_name = list(dept_name)
	single_dept = dept_name[0]
	return render(request,'sub_dept_list.html',{'sub_depts':sub_depts,'single_dept':single_dept})
#it collects all the sub depts under a particular dept and sends it the html page for rendering.


def tenders(request, pk):
	tenders_list= tender.objects.filter(Sub_Id=pk)
	return render(request,'tender_list.html',{'tenders_list':tenders_list})
#it collects all the tenders under a particular sub dept and sends it the html page for rendering.

def bid(request,pk):
	
	bidding_list= tender.objects.filter(id=pk)
	bidding_object= bidding.objects.filter(t_id=pk).order_by('b_price')
	
	return render(request,'bid_list.html',{'bidding_list':bidding_list,'bidding_object':bidding_object})	
#it gets all the bids under particular tender and sends to html page to render it.


def bid_now(request,pk_t,comp_name):
	
	temp_check=bidding.objects.all()

	date_ver = tender.objects.get(id=pk_t)
	ver_bool = date_ver.expired()
	if (not ver_bool):
		msg="The last date for bidding has been expired..!"
		return render(request,'error.html',{'msg':msg})
	
	for temp in temp_check:
		if(comp_name==temp.c_id.c_name and int(pk_t)==int(temp.t_id.id)):
			msg="Your Company has already done bid once!! There is no second chance"
			return render(request,'error.html',{'msg':msg})
	
	if request.method == 'POST':
		bidding_price = request.POST['bidding_price']
		bidding_description = request.POST['bidding_description']
		topic = bidding.objects.create(
			t_id=tender.objects.get(id=pk_t),
			c_id=company.objects.get(c_name=comp_name),
			b_price = bidding_price,
			b_description = bidding_description
			)
		
		return redirect('bid',pk=pk_t)
	return render(request,'bid_forms.html')
#it gets the tender id and company name..
#if they have already bid once they will not be given another chance.
#if not it will take their price and description and create a bid object.
#admin is made not allowed to bid.




def complaints(request):
	if request.method == 'POST':
		compl_name = request.POST['compl_name']
		compl_description = request.POST['compl_description']
		topic = complaint.objects.create(
			compl_name = compl_name,
			compl_description = compl_description
			)
		return redirect('home')
	return render(request,'complaints.html')
#it is a module which takes the complaint name and its description from the form and make it into a object of complaint type. 
#after taking complaint it redirects to the home page.

