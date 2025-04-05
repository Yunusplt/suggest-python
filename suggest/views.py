from django.shortcuts import render
from django.http import JsonResponse
from suggest.models import Products
from django.db.models import Q

# View function: render the search page
def search_page(request):
    return render(request, "suggest/search.html")

# API view: return the search results as JSON
def api_search(request):
    query = request.GET.get("q", "").strip()
    product_results = []
    category_results = []

    if query:
        #  filter products by name
        product_filtered = Products.objects.filter(
            Q(product_name__icontains=query)
        )[:6]  # first 6 products

        product_results = [
            {"name": p.product_name, "category": p.category, "price": float(p.price)}
            for p in product_filtered
        ]

        # filter categories by name
        category_filtered = Products.objects.filter(
            Q(category__icontains=query)
        )[:6]  # first 6 categories

        category_results = [
            {"name": p.product_name, "category": p.category, "price": float(p.price)}
            for p in category_filtered
        ]

    # return the results as JSON
    return JsonResponse({
        "product_results": product_results,
        "category_results": category_results
    })
