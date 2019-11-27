from django.db import models

from django.contrib.auth.models import User

# it is a table which has the department name and image related to that department
class dept_master(models.Model):
	d_name=models.CharField(max_length=30)
	d_image= models.CharField(max_length=50,null=True)
	def __str__(self):
		return (self.d_name)

#it is a table which has the sub dept name and image also it has a forign key from dept_master table which indicate under which dept this comes. 
class sub_dept(models.Model):
	sub_dept_name=models.CharField(max_length=30)
	sub_image= models.CharField(max_length=50,null=True)
	D_Id=models.ForeignKey(dept_master, related_name='department_id', on_delete=models.CASCADE,)
	def __str__(self):
		return (self.sub_dept_name)
		
#it is a table having:
#tender name,image,start date,end date
#it also has forignkeys from dept_master and sub_dept which helps to track under which dept and sub-dept it belongs. 
class tender(models.Model):
	t_name=models.CharField(max_length=30)
	D_Id=models.ForeignKey(dept_master, related_name='department_id1', on_delete=models.CASCADE,)
	Sub_Id=models.ForeignKey(sub_dept, related_name='sub_department_id', on_delete=models.CASCADE,)
	t_description = models.CharField(max_length=100)
	t_image= models.CharField(max_length=50,null=True)
	t_start_period=models.DateTimeField(null=True)
	t_price=models.FloatField()
	t_end_date = models.DateTimeField(null=True)
	def __str__(self):
		return (self.t_name)

	def expired(self):
		import datetime
		from django.utils import timezone
		if self.t_end_date < timezone.now():
			return False
		else:
			return True


#company is the user who wants to bid.
#every company should have a unique registration number.
class company(models.Model):
	#c_user = models.ForeignKey(User,related_name = 'company_user',on_delete=models.CASCADE,null=True,default=0)
	c_name=models.CharField(max_length=30, null=True)
	c_reg_no=models.CharField(max_length=12, unique=True)
	def __str__(self):
		return (self.c_name)



#Complaints is the table which holds the name of the complaint and description about it.
#it is not linked to user/company so that it is anonymous and even admin should not find out.
class complaint(models.Model):
	compl_name = models.CharField(max_length=30, null=True)
	compl_description = models.CharField(max_length=250, null=True)
	def __str__(self):
		return (self.compl_name)


#bidding is the important table linking the company and tender
#it creates a link between the company that has bid and the tender that it has bid.
class bidding(models.Model):
	c_id = models.ForeignKey(company,related_name = 'company_id',on_delete=models.CASCADE,null=False,default=None)
	t_id = models.ForeignKey(tender,related_name = 'tender_id',on_delete=models.CASCADE,)
	b_price = models.FloatField()
	b_description = models.CharField(max_length=100)
	

