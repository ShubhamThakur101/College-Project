from django.urls import path
from .views import Home,Add_Details,Delete_Tdata

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('add_details/',Add_Details.as_view(), name='add_details'),
    path('Delete_Tdata/',Delete_Tdata.as_view(),name='Delete_Tdata')
]
