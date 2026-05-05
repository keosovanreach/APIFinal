from django.urls import path
from . import views
from .views import * 

urlpatterns = [
    # path('', views.home),
    # path('roles/', views.roles),
    path('APIRoles/', RolesListCreate.as_view(), name='APIRoles'),
    path('APIRoles/<int:pk>/', RolesUpdateDelete.as_view(), name='APIRoles'),
    
   # Users
    path('users/', views.UserListCreate.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    # Categories
    path('categories/', views.CategoryListCreate.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),

    # Suppliers
    path('suppliers/', views.SupplierListCreate.as_view()),
    path('suppliers/<int:pk>/', views.SupplierDetail.as_view()),

    # Customers
    path('customers/', views.CustomerListCreate.as_view()),
    path('customers/<int:pk>/', views.CustomerDetail.as_view()),

    # Products
    path('products/', views.ProductListCreate.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),

    # Purchase Orders
    path('purchase-orders/', views.PurchaseOrderListCreate.as_view()),
    path('purchase-orders/<int:pk>/', views.PurchaseOrderDetail.as_view()),

    # Purchase Order Items
    path('purchase-order-items/', views.PurchaseOrderItemListCreate.as_view()),
    path('purchase-order-items/<int:pk>/', views.PurchaseOrderItemDetail.as_view()),

    # Goods Receipts
    path('goods-receipts/', views.GoodsReceiptListCreate.as_view()),
    path('goods-receipts/<int:pk>/', views.GoodsReceiptDetail.as_view()),

    # Sales
    path('sales/', views.SaleListCreate.as_view()),
    path('sales/<int:pk>/', views.SaleDetail.as_view()),

    # Sale Items
    path('sale-items/', views.SaleItemListCreate.as_view()),
    path('sale-items/<int:pk>/', views.SaleItemDetail.as_view()),

    # Payments
    path('payments/', views.PaymentListCreate.as_view()),
    path('payments/<int:pk>/', views.PaymentDetail.as_view()),

    # Stock Movements
    path('stock-movements/', views.StockMovementListCreate.as_view()),
    path('stock-movements/<int:pk>/', views.StockMovementDetail.as_view()),

    # Supplier Reviews
    path('supplier-reviews/', views.SupplierReviewListCreate.as_view()),
    path('supplier-reviews/<int:pk>/', views.SupplierReviewDetail.as_view()),
]

         
   

