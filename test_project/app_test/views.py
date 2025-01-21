from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Item

def item_list(request):
    try:
        items = Item.objects.all()
        return render(request, 'item_list.html', {'items': items})
    except Exception as e:
        return JsonResponse({'error': 'An error occurred while fetching items.'}, status=500)

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item_details.html', {'item': item})
