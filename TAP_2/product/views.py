from django.shortcuts import render, redirect
from .models import Drink, Category
# Create your views here.

def home(request):
    return redirect('/product')



def product(request):
    if request.method == 'GET':

        return render(request, 'main.html')

    elif request.method == 'POST':
        checkbox1 = request.POST.get('checkbox1', '')
        checkbox2 = request.POST.get('checkbox2', '')
        checkbox3 = request.POST.get('checkbox3', '')
        if checkbox1 != '':
            drink_category = checkbox1
        elif checkbox2 != '':
            drink_category = checkbox2
        elif checkbox3 != '':
            drink_category = checkbox3
        else:
            drink_category = ''
        print(drink_category)
        category = Category.objects.get(category_name=drink_category)
        my_drink = Drink.objects.filter(drink_category=category)
        return render(request, 'main.html', {'drink': my_drink})