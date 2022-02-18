from django.urls import path
from django_crud.views import *

urlpatterns = [
      path('',index,name="index"),
      path('<int:product_id>/',index,name="update"),
      path('add-product/',addProductForm,name="Add-Product-Form"),
      path('delete/<int:id>',delete,name="Delete-Product")
   ]
