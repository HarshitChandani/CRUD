from django.shortcuts import render,redirect,HttpResponse
from django_crud.models import Product


def index(request,product_id=0):
   '''
      GET request: views product list operation.
      POST request: insert new product operation. 
      if product_id is 0:
         < insert operation >
      else:
         < update operation > 
   '''
   if request.method == 'GET':
      if product_id == 0:
         data = Product.objects.all()
         template = "index.html"
      else:
         data = Product.objects.get(id=product_id)
         template = "add.html"
      return render(request,template,{'product_data':data})
   else:   
      product_name = request.POST['product_name']
      product_price = request.POST['product_price']
      product_quantity = request.POST['product_quantity']
      if product_id == 0:
         Product.objects.create(
            name=product_name, 
            price=product_price, 
            qty=product_quantity
         )
      else:
         # Update POST operation .
         Product.objects.filter(id=product_id).update(
            name=product_name, 
            price=product_price,
            qty =product_quantity
            )
      return redirect("/")


def addProductForm(request):
   return render(request,"add.html")


def delete(request,id:int):
   deleted_product = Product.objects.get(id=id)
   deleted_product.delete()
   return redirect("/")   
