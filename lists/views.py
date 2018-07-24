from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        itemtext = request.POST['item_text']
        print('param : ' + itemtext)
        Item.objects.create(text=itemtext)
        return redirect('/')

    items = Item.objects.all()
    for item  in items:
        print(item.text)

    return render(request, 'home.html', {'items': items})