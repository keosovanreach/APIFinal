from datetime import date
import email
from pydoc import text
from unicodedata import decimal
from weakref import ref

from django.db import models


# Create your models here.
class Roles(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# Users
class User(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)

    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# Categories
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Suppliers
class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    supplier_code = models.CharField(max_length=50, unique=True)

    name = models.CharField(max_length=150)
    contact_person = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    address = models.TextField()
    tax_id = models.CharField(max_length=50, blank=True, null=True)

    supplier_logo = models.ImageField(upload_to='suppliers/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Customers
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    customer_code = models.CharField(max_length=50, unique=True)

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)

    email = models.EmailField(unique=True)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Products
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=100, unique=True)

    name = models.CharField(max_length=150)
    description = models.TextField()

    unit_of_measure = models.CharField(max_length=20)

    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    stock_quantity = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    product_image = models.ImageField(upload_to='products/', null=True, blank=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    discount_type = models.CharField(max_length=20, blank=True, null=True)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


# Purchase Orders
class PurchaseOrder(models.Model):
    id = models.AutoField(primary_key=True)
    po_number = models.CharField(max_length=50, unique=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    order_date = models.DateField()
    expected_delivery_date = models.DateField()

    status = models.CharField(max_length=50)

    tax_amount = models.DecimalField(max_digits=12, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.po_number


# Purchase Order Items
class PurchaseOrderItem(models.Model):
    id = models.AutoField(primary_key=True)

    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.purchase_order.po_number} - {self.product.name}"


# Goods Receipt
class GoodsReceipt(models.Model):
    id = models.AutoField(primary_key=True)

    grn_number = models.CharField(max_length=50, unique=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)

    received_date = models.DateField()
    received_by = models.ForeignKey(User, on_delete=models.CASCADE)

    delivery_note_image = models.ImageField(upload_to='grn/', null=True, blank=True)

    def __str__(self):
        return self.grn_number


# Sales
class Sale(models.Model):
    id = models.AutoField(primary_key=True)

    sale_number = models.CharField(max_length=50, unique=True)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    sale_date = models.DateField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.CharField(max_length=50)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.sale_number


# Sale Items
class SaleItem(models.Model):
    id = models.AutoField(primary_key=True)

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.sale.sale_number} - {self.product.name}"


# Payments
class Payment(models.Model):
    id = models.AutoField(primary_key=True)

    payment_reference = models.CharField(max_length=100)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)

    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    method = models.CharField(max_length=50)
    receipt_image = models.ImageField(upload_to='payments/', null=True, blank=True)

    status = models.CharField(max_length=50)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.payment_reference


# Stock Movements
class StockMovement(models.Model):
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    movement_type = models.CharField(max_length=20)  # IN / OUT
    quantity = models.PositiveIntegerField()

    reference_type = models.CharField(max_length=50)
    reference_id = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movement_type} - {self.product.name}"


# Supplier Reviews
class SupplierReview(models.Model):
    id = models.AutoField(primary_key=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)

    rating = models.IntegerField()
    comments = models.TextField(blank=True, null=True)

    delivery_on_time = models.BooleanField(default=True)
    product_quality_score = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.supplier.name} - {self.rating}"