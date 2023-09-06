from django.db import models
from django.contrib.auth.models import User,AbstractUser
import datetime 
import os
import random


# Create your models here.
class User(AbstractUser):
    # email = models.EmailField(unique=True)
    is_admin= models.BooleanField('Is admin',default=False)
    is_enquiry = models.BooleanField('Is enquiry',default=False)
    is_account = models.BooleanField('Is account',default=False)
    is_it = models.BooleanField('Is it',default=False)
    is_hr = models.BooleanField('Is hr',default=False)
    is_training = models.BooleanField('Is training',default=False)

class Cource(models.Model):
    Cource_name=models.CharField(max_length=100,null=True)    
    fees=models.BigIntegerField()
    durations=models.CharField(max_length=50,null=True)
  
    def __str__(self):
        return f"{self.Cource_name}"

class Enquiry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='enquiry',null=True)
    Full_Name=models.CharField(max_length=250,default="")
    gender=models.CharField(max_length=10)
    Email_Address=models.EmailField()
    Contact_Number=models.IntegerField() 
    Permanent_Address=models.TextField(blank=True,null=True,default='')
    Date_of_Birth=models.DateField(auto_now_add=False,null=True,blank=True)   
    massage=models.TextField(blank=True,null=True)
    Whatsapp_Number=models.IntegerField(blank=True,null=True)
    Alternate_Number=models.IntegerField(blank=True,null=True)
    How_did_you_hear_about_us=models.CharField(null=True,max_length=50)
    qualification=models.CharField(max_length=50,null=True,blank=True)
    Technical_Skills=models.CharField(max_length=150,null=True,blank=True)
    Certification_Done=models.CharField(max_length=200,null=True,blank=True)
    Area_of_Intrest=models.CharField(max_length=200,null=True,blank=True)
    reference=models.CharField(max_length=100,null=True,blank=True)
    remark=models.CharField(max_length=100,null=True,blank=True)
    Training_Mode=models.CharField(max_length=50,blank=True,null=True)
    Office_Location_Preference=models.CharField(max_length=50,null=True,blank=True)
   
    STATUS = (
        ('Finalized', 'Finalized'),
        ('Pending', 'Pending'),
        ('Informed_On_whatsapp','Informed_On_whatsapp')
        
    )
    enquiry_Status = models.TextField(max_length=100, choices=STATUS, default="Pending",null=True)
    Cource_name=models.ForeignKey(Cource,on_delete=models.CASCADE,null=True,blank=True)
    
class Training_Enquiry(models.Model):
     name=models.CharField(max_length=250,default="")
     email=models.EmailField()
     phone=models.IntegerField()
     course=models.CharField(max_length=200)
     durations=models.CharField(max_length=50,null=True)
     interest=models.CharField(max_length=200)
     
class Development_Enquiry(models.Model):
     name=models.CharField(max_length=250,default="")
     email=models.EmailField()
     message=models.CharField(max_length=200)   

class Reason_follow(models.Model):
    name=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

class reason_for_follow_up(models.Model):
    enquiry=models.ForeignKey(Enquiry,on_delete=models.CASCADE,null=True,blank=True)
    reason =models.ForeignKey('Reason_follow',on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(default=datetime.date.today)   
    time = models.TimeField(auto_now=True)
    remark = models.CharField(max_length=100,null=True)
    STATUS = (
        ('FollowUp Done', 'FollowUp Done'),
        ('Pending', 'Pending'),
        )
    Followup_Status = models.TextField(max_length=100, choices=STATUS, default="Pending",null=True)
    Enroll_flag=models.BooleanField(default=False)
    
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account',null=True)
    enquiry=models.ForeignKey(Enquiry,on_delete=models.CASCADE,null=True,blank=True)
    total_installment=models.IntegerField()
    pay_date=models.DateTimeField(default=datetime.date.today)
    first_installment=models.FloatField(blank=True,null=True)
    payment_mode=models.CharField(max_length=50,null=True,blank=True)
    receipt=models.ImageField(upload_to='media/')
    second_installment=models.FloatField(blank=True,null=True)
    second_date=models.DateField(blank=True,null=True)
    third_installment=models.FloatField(blank=True,null=True)
    third_date=models.DateField(blank=True,null=True)
    four_installment=models.FloatField(blank=True,null=True)
    four_date=models.DateField(blank=True,null=True)
    STATUS=(
        ('Pending','Pending'),
        ('first_installment','first_installment'),
        ('second_installment','second_installment'),
        ('third_installment','third_installment'),
        ('fourth_installment','fourth_installment'),
        ('installment_completed','installment_completed')
    )
    payment_status= models.TextField(max_length=100, choices=STATUS, default="Pending",null=True)
    account_remark=models.CharField(max_length=500,null=True)
    amount=models.IntegerField(blank=True,null=True,default=0)
    amount_date=models.DateField(default=datetime.date.today)
    amount_remaining = models.PositiveIntegerField(blank=True,null=True)
    total_amount=models.FloatField(blank=True,null=True)
class Category(models.Model):
    cname=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return f"{self.cname}"

class Assert_create(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    a_name=models.CharField(max_length=50,null=True,blank=True)
    a_description=models.TextField(max_length=500,null=True,blank=True)
    make_year=models.CharField(max_length=50)
    model_name=models.CharField(max_length=500,blank=True,null=True)
    serial_no=models.CharField(max_length=50,null=True,blank=True)
    condition=models.CharField(null=True,blank=True,max_length=10)
    system=models.CharField(null=True,blank=True,max_length=10)
    asset_photo=models.ImageField(upload_to='media/')
   
    def __str__(self):
        return self.asset_photo

class Desktop(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    enquiry=models.ForeignKey(Enquiry,on_delete=models.CASCADE,null=True,blank=True)
    model_name=models.CharField(max_length=500,blank=True,null=True)
  
    def __str__(self) -> str:
        return self.model_name

class Allocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='it',null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    desktop=models.ForeignKey(Desktop,on_delete=models.CASCADE,null=True,blank=True)
    enquiry=models.ForeignKey(Enquiry,on_delete=models.CASCADE,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    model_name=models.CharField(max_length=500,blank=True,null=True)
    serial_no=models.CharField(max_length=50,null=True,blank=True)
    L_condition=models.CharField(null=True,blank=True,max_length=10)
    L_purpose=models.CharField(max_length=200,null=True,blank=True)
    L_allocation_date=models.DateField(default=datetime.date.today)
    L_photos=models.ImageField(upload_to='media/')
    STATUS=(
        ('allocated','allocated'),
        ('not_allocated','not_allocated'),
        ('scrap','scrap'),
      
    )
    system_status=models.TextField(max_length=100, choices=STATUS, default="not_allocated",null=True)
    def __str__(self) -> str:
        return self.model_name,self.L_photos
    
class system_details(models.Model):
    desktop=models.ForeignKey(Desktop,on_delete=models.CASCADE,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    model_name=models.CharField(max_length=500,blank=True,null=True)
    serial_no=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return self.model_name

class Compulsory(models.Model):
    documment_name=models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='media/',default="",null=True)
    def __str__(self) -> str:
        return self.documment_name

class Optional(models.Model):
    documment_name=models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='media/',default="",null=True)
    def __str__(self) -> str:
        return self.documment_name
    
class Documetation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='hr',null=True)
    enquiry=models.ForeignKey(Enquiry,on_delete=models.CASCADE,null=True,blank=True)
    compulsory=models.ForeignKey(Compulsory,on_delete=models.CASCADE,null=True,blank=True)
    optional=models.ForeignKey(Optional,on_delete=models.CASCADE,null=True,blank=True)
    photos=models.ImageField(upload_to='media/',default="")
    image=models.ImageField(upload_to='media/',default="")
    appointment=models.ImageField(upload_to='media/',default="",null=True)
    account_link=models.CharField(max_length=200,null=True,blank=True)
    post_link=models.CharField(max_length=200,null=True,blank=True)
    STATUS=(
    ('kit_allocated','kit_allocated'),
    ('Not_allocated','Not_allocated')
    )
    welcome=models.TextField(max_length=100, choices=STATUS, default="not_allocated",null=True)
    I_STATUS=(
    ('Intro_Done','Intro_Done'),
    ('Not_Done','Not_Done')
    )
    intro=models.TextField(max_length=100, choices=I_STATUS, default="Not_Done",null=True)
    
class Trainer(models.Model):
    trainer_name=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self) -> str:
        return self.trainer_name

    
class Training(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='training',null=True)
    trainer_name=models.ForeignKey(Trainer,on_delete=models.CASCADE,null=True,blank=True)
    enquiry=models.ForeignKey(Enquiry,on_delete=models.CASCADE,null=True,blank=True)
    STATUS=(
        ('Pending','Pending'),
        ('Phase_I_Completed','Phase_I_Completed'),
        ('Phase_II_Completed','Phase_II_Completed'),
        ('Phase_III_Completed','Phase_III_Completed'),
        ('Phase_IV_Completed','Phase_IV_Completed'),
    )
    training_status= models.TextField(max_length=100, choices=STATUS, default="Pending",null=True)
    phase_I=models.CharField(max_length=500,null=True,blank=True)
    phase_II=models.CharField(max_length=500,null=True,blank=True)
    phase_III=models.CharField(max_length=500,null=True,blank=True)
    phase_IV=models.CharField(max_length=500,null=True,blank=True)
    date1=models.DateField(default=datetime.date.today)
    date2=models.DateField(default=datetime.date.today)
    date3=models.DateField(default=datetime.date.today)
    date4=models.DateField(default=datetime.date.today)

class Project(models.Model):
    enquiry=models.ForeignKey(Enquiry,on_delete=models.CASCADE,null=True,blank=True)
    topic_name=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    date=models.DateField(default=datetime.date.today)
    image=models.ImageField(upload_to='media/',default="")
    STATUS=(
        ('Pending','Pending'),
        ('Phase_I_Completed','Phase_I_Completed'),
        ('Phase_II_Completed','Phase_II_Completed'),
        ('Phase_III_Completed','Phase_III_Completed'),
        ('Phase_IV_Completed','Phase_IV_Completed'),
    )
    project_status= models.TextField(max_length=100, choices=STATUS, default="Pending",null=True)
    phase_I=models.CharField(max_length=500,null=True,blank=True)
    phase_II=models.CharField(max_length=500,null=True,blank=True)
    phase_III=models.CharField(max_length=500,null=True,blank=True)
    phase_IV=models.CharField(max_length=500,null=True,blank=True)
    date1=models.DateField(default=datetime.date.today)
    date2=models.DateField(default=datetime.date.today)
    date3=models.DateField(default=datetime.date.today)
    date4=models.DateField(default=datetime.date.today)
    
    
def upload_path(instance, filename):
	if instance.picture:
		fileid = instance.user.id
	else:
		random.seed(datetime.now())
		fileid = random.randint(int(1e9), int(1e10))
	new_filename = 'p{0}_{1}'.format(fileid, filename)
	path = 'profile_images'
	return os.path.join(path, new_filename)
    
    
class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True,default='',on_delete=models.CASCADE)
	picture = models.ImageField(upload_to=upload_path, blank=True,default='')

	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.user.username