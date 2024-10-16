from .models import Cart,CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart = Cart.objects.filter(cart_id = Cart.cart_id)
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user = request.user)
            else:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                cart_items = CartItem.objects.filter(cart=cart, is_active=True)
                # print(cart)
                
            for cart_item in cart_items:
                cart_count += cart_item.quantity
            return dict(cart_count = cart_count)
        except cart.DoesNotExist:
            cart_count = 0
            
    return dict(cart_count = cart_count)