from django.contrib import admin
from .models import Unit,Unit_type,Unit_state,Address,Property,Employee,In_charge_of,Geofence,File_attachment
from .models import Owner,Property_file_attachment,Contract,Employee_job,Contract_type,Estate_contract
from .models import Item_category,Supplier,Item,Invoice,Invoice_item,transaction_type,Transaction




# Register your models here.

admin.site.register(Unit)
admin.site.register(Unit_type)
admin.site.register(Unit_state)
admin.site.register(Address)
admin.site.register(Property)
admin.site.register(Employee)
admin.site.register(In_charge_of)
admin.site.register(Geofence)
admin.site.register(File_attachment)
admin.site.register(Property_file_attachment)
admin.site.register(Employee_job)
admin.site.register(Owner)
admin.site.register(Contract)
admin.site.register(Estate_contract)
admin.site.register(Contract_type)
admin.site.register(Item_category)
admin.site.register(Supplier)
admin.site.register(Item)
admin.site.register(Invoice)
admin.site.register(Invoice_item)
admin.site.register(transaction_type)
admin.site.register(Transaction)








