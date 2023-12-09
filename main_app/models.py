from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import uuid

# Create your models here.


class customers(models.Model):
    id = models.AutoField(primary_key=True)
    customer_unique = models.UUIDField(default=uuid.uuid4,editable=False)
    first_name = models.CharField(max_length=1000,blank=True,null=True)
    last_name = models.CharField(max_length=1000,blank=True,null=True)
    email = models.EmailField()
    picture = models.ImageField(blank=True,null=True)
    email_verified = models.BooleanField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name+ " "+ self.last_name
    

class users(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(customers,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    is_supueruser = models.BooleanField();

class companies(models.Model):
    id = models.AutoField(primary_key=True)
    company_unique = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1000)
    customer = models.ForeignKey(customers, on_delete=models.CASCADE)
    gstin = models.CharField(max_length=1000)
    logo = models.ImageField(null=True,blank=True)
    address = models.CharField(max_length=10000,null=True,blank=True)

    def __str__(self):
        return self.name+" "+ self.customer.first_name



class user_access(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    access_rights = models.ForeignKey(companies,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.user.name + " "+ self.access_rights.name

# class customers(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=1000)
#     contact = models.CharField(max_length=100)
#     email = models.EmailField()
    
    



class clients(models.Model):
    id = models.AutoField(primary_key=True)
    client_unique = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1000)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.ForeignKey(companies,on_delete=models.CASCADE)
    gstin = models.CharField(max_length=1000)
    address = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + str(self.client_unique)




class sales(models.Model):
    choice = [
        ('CASH',"CASH"),
        ('CHEQUE','CHEQUE')
    ]
    id = models.AutoField(primary_key=True)
    sale_unique = models.UUIDField(default=uuid.uuid4, editable=False)
    company = models.ForeignKey(companies,on_delete=models.CASCADE)
    client = models.ForeignKey(clients,on_delete=models.CASCADE)
    invoice_date = models.DateField()
    invoice_id = models.CharField(max_length=100)
    tax_percent = models.FloatField()
    tax_amount = models.FloatField()
    discount_percent = models.FloatField()
    discount_amount = models.FloatField()
    subtotal = models.FloatField(max_length=10000000)
    currency = models.CharField(max_length=100000)
    due_date = models.DateField(null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank = True)
    total_amount = models.FloatField()
    amount_received = models.FloatField(null=True,blank=True)
    payment_type = models.CharField(max_length=1000,choices=choice)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    front_random_id = models.CharField(max_length=100,null=True, blank=True)
    amount_in_words = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.company.name + " "+ str(self.invoice_date) + " " + self.company.name+ " "+ str(self.client.client_unique) + " " + str(self.sale_unique)


class salesItem(models.Model):
    id = models.AutoField(primary_key=True)
    sale = models.ForeignKey(sales,on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.sale.company.name + " "+self.name+str(self.sale.total_amount)
    


class transactions(models.Model):
    id = models.AutoField(primary_key=True)
    transaction_id = models.CharField(max_length=1000)
    client = models.ForeignKey(clients,on_delete=models.CASCADE)
    company = models.ForeignKey(companies,on_delete=models.CASCADE)
    total_amount = models.CharField(max_length=10000)
    description = models.TextField(blank=True,null=True)
    receipt_no = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)


    
class payment(models.Model):
    choice = [
        ('CASH',"CASH"),
        ('CHEQUE','CHEQUE')
    ]
    id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=1000,choices=choice)
    amount = models.CharField(max_length=10000)
    transaction_id = models.ForeignKey(transactions,on_delete=models.CASCADE)


