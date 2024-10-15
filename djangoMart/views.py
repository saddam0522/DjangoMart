from django.shortcuts import render
from catagory.models import Category
from store.models import Product
from django.core.paginator import Paginator
def home(request):
    products = Product.objects.filter(is_available = True)
    page = request.GET.get('page')
    paginator = Paginator(products, 12)
    paged_product = paginator.get_page(page)
    

    categories = Category.objects.all()
    
    
    context = {'products' : paged_product, 'categories':categories}

    return render(request,'index.html', context)