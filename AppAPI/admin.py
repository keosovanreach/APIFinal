from django.contrib import admin
from .models import *
 
# Register your models here.
admin.site.register(Roles)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItem)
admin.site.register(GoodsReceipt)
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Payment)
admin.site.register(StockMovement)
admin.site.register(SupplierReview)



admin.site.site_header = 'S.Management System'
admin.site.site_title = 'Supplier Management System Admin'
admin.site.index_title = 'Welcome to Supplier Management System Admin'
