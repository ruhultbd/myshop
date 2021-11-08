from django.db.models import Sum

def categories(request):
    from product.models import Category
    return {'categories': Category.objects.order_by('name')}

def brands(request):
    from home.models import Brand
    return {'brands': Brand.objects.order_by('name')}

def cart_items(request):
    from product.models import Cart
    cartData = {}
    totalItem = 0
    totalPrice = 0
    if 'sessionId' in request.session:
         sessionId = request.session['sessionId']
         cartData = Cart.objects.filter(session_id=sessionId).order_by('-id')
         totalItem = len(cartData)

         amounts = Cart.objects.values_list('total_price', flat=True)
         totalPrice = sum(amounts)

    return {'cart_items': cartData, 'total_cart_item': totalItem, 'cart_item_total_price': totalPrice}
