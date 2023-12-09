
from django.urls import path
from . import views


urlpatterns = [
    path('authentication_data',views.authenticationData),
    path('get_units',views.getUnits),
    path('get_tax_units',views.get_tax_units),
    path('get_client_data',views.get_client_data),
    path('get_recent_sales',views.getRecentSales),
    path('sales_data',views.salesData),
    path('check_invoice_id/<str:id>',views.checkInvoiceId)
]