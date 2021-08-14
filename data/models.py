from django.db import models
from datetime import datetime


# Create your models here.

#super user => login : root  \\ pwd : badiscord

class Item_category(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20,null=True)    
    def __str__(self):
         return self.uuid
    class Meta:
        verbose_name = 'Item category'


class Supplier(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    def __str__(self):
         return self.uuid
    class Meta:
        verbose_name = 'Supplier'



class Item(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20,null=True)
    default_price = models.DecimalField(max_digits=4,decimal_places=3)
    supplier_uuid = models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    item_category_uuid = models.ForeignKey(Item_category,on_delete=models.CASCADE,null=True)
    def __str__(self):
         return self.uuid
    class Meta:
        verbose_name = 'Item'

class Invoice(models.Model):
    uuid = models.UUIDField(primary_key=True)
    invoice_number = models.CharField(max_length=20,null=True)
    issued_by = models.CharField(max_length=20,null=True)
    issued_to = models.CharField(max_length=20,null=True)
    total_amount = models.DecimalField(max_digits=4,decimal_places=3)
    details = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(default=datetime.now)
    paid_date = models.DateTimeField(default=datetime.now)
    #type enum
    tax_cut_percentage = models.IntegerField(null=True)
    def __str__(self):
         return self.uuid
    class Meta:
        verbose_name = 'Invoice'


class Invoice_item(models.Model):
    uuid = models.UUIDField(primary_key=True)
    count = models.CharField(max_length=20,null=True)
    item_uuid = models.UUIDField()
    unit_price = models.DecimalField(max_digits=4,decimal_places=3)
    invoice_uuid = models.ForeignKey(Invoice, on_delete=models.CASCADE,null=True)

    def __str__(self):
         return self.uuid
    class Meta:
        verbose_name = 'Invoice_item'


class transaction_type(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
         return self.name
    class Meta:
        verbose_name = 'Transaction type'


class Transaction(models.Model):
    uuid = models.UUIDField(primary_key=True)
    transaction_type = models.ForeignKey(transaction_type, on_delete=models.CASCADE,null=True)
    transaction_date = models.DateTimeField(default=datetime.now)
    details = models.TextField(null=True,blank=True)
    def __str__(self):
         return self.name
    class Meta:
        verbose_name = 'Transaction'



class Contract_type(models.Model):    
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
         return self.name
    class Meta:
        verbose_name = 'Contract type'


class Contract(models.Model):
    uuid = models.UUIDField(primary_key=True)
    contract_type = models.ForeignKey(Contract_type, on_delete=models.CASCADE,null=True)
    payment_frequency = models.DecimalField(max_digits=4,decimal_places=3)
    payment_amount = models.DecimalField(max_digits=4,decimal_places=3)
    date_signed = models.DateTimeField(default = datetime.now)
    start_date = models.DateTimeField(default = datetime.now)
    end_date = models.DateTimeField(default = datetime.now)
    fee_amount = models.DecimalField(max_digits=2,decimal_places=2)
    fee_percentage = models.IntegerField()
    tranaction_uuid = models.ForeignKey(Transaction, on_delete=models.CASCADE,null=True)
    invoice_uuid = models.ForeignKey(Invoice, on_delete=models.CASCADE,null=True)
    def __str__(self):
         return self.name
    class Meta:
        verbose_name = 'Contract'

class Employee_job(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20,null =True)
    def __str__(self):
         return self.name
    class Meta:
        verbose_name = 'Employee Job'



class Owner(models.Model):
    uuid = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=10,null =True)
    first_name = models.CharField(max_length=10,null =True)
    phone_number = models.CharField(max_length=10,null =True)
    def __str__(self):
         return self.uuid
    class Meta:
        verbose_name = 'Owner'

class Address(models.Model):
    uuid = models.UUIDField(primary_key=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    def __str__(self):
         return self.uuid
    class Meta:
        verbose_name = 'Address'

class File_attachment(models.Model):    
    uuid = models.UUIDField(primary_key=True)
    formats = models.enums
    file_path = models.CharField(max_length=50)
    def __str__(self):
         return self.uuid
    class Meta:
        verbose_name = 'File attachment'
    

class Property(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    floor_space = models.CharField(max_length=20)
    address_uuid = models.OneToOneField(Address, on_delete=models.CASCADE)
    attachment_uuid = models.OneToOneField(Owner, on_delete=models.CASCADE)
    def __str__(self):
         return self.name
    class Meta:
        verbose_name = 'Property'

class Estate_contract(models.Model):
    uuid = models.UUIDField(primary_key=True)
    propery_uuid = models.ForeignKey(Property, on_delete=models.CASCADE)
    Contract_uuid = models.ForeignKey(Contract, on_delete=models.CASCADE)
    def __str__(self):
         return self.uuid
    class Meta:
        verbose_name = 'Estate contract'

class Property_file_attachment(models.Model):
    uuid = models.UUIDField(primary_key=True)
    file_attachment_uuid = models.ForeignKey(File_attachment, on_delete=models.CASCADE)
    property_uuid = models.ForeignKey(Property, on_delete=models.CASCADE,null = True)
    def __str__(self):
         return self.name
    class Meta:
        verbose_name = 'Property File attachment'



class Geofence(models.Model):  
    uuid = models.UUIDField(primary_key=True)
    geoence_file_uuid = models.OneToOneField(File_attachment, on_delete=models.CASCADE)
    property_id = models.OneToOneField(Property, on_delete=models.CASCADE,null = True)
    def __str__(self):
         return self.name
    class Meta:
        verbose_name = 'Geofence'

 
class Employee(models.Model):
    uuid = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    phone_number = models.DecimalField(decimal_places=8,max_digits=8)
    employee_job = models.ForeignKey(Employee_job, on_delete=models.CASCADE,null = True)
    employee_contract = models.OneToOneField(Contract, on_delete=models.CASCADE,null = True)
    def __str__(self):
         return self.uuid
    class Meta:
        verbose_name = 'Employee'
    

class In_charge_of(models.Model):
    uuid = models.UUIDField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE )
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE )
    start_date = models.DateTimeField(default = datetime.now)
    end_date = models.DateTimeField(default = datetime.now)
    def __str__(self):
         return self.uuid
    class Meta:
        verbose_name = 'In charge of'


class Unit_state(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
         return self.name
    class Meta:
        verbose_name = 'Unit state'

class Unit_type(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
         return self.uuid   ## afficher par uuid
    class Meta:
        verbose_name = 'Unit type'


class Unit(models.Model):
    uuid = models.UUIDField(primary_key=True,verbose_name = 'Uuid number')

    appartment_number = models.IntegerField(null = True)

    pets_allowed = models.BooleanField(null = True)
    number_of_bedrooms = models.IntegerField(null = True)
    number_of_bathrooms = models.IntegerField(null = True)
    number_of_garages = models.IntegerField(null = True)
    unit_type = models.ForeignKey(Unit_type, on_delete = models.CASCADE,null=True)
    unit_state = models.ForeignKey(Unit_state, on_delete = models.CASCADE,null=True)

    def __str__(self):
         return self.uuid

    class Meta:
        verbose_name = 'Unit'



    

