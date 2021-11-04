
def getCategories(request):
    from product.models import Category
    return {'categories': Category.objects.all()}
