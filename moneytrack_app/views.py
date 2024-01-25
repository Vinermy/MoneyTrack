from django.shortcuts import render, redirect

from moneytrack_app.forms import CategoryCreationForm
from moneytrack_app.models import Category


# Create your views here.
def index(request):

    ctx = {
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', ctx)


def settings(request):
    if request.method == 'POST':
        match request.POST.get('form-type'):
            case 'add-category':
                form = CategoryCreationForm(request.POST)
                form.save()
            case 'delete-category':
                id = request.POST.get('category-id')
                Category.objects.get(id=id).delete()

        return redirect('settings')


    ctx = {
        'categories': Category.objects.all()
    }

    return render(request, 'settings.html', ctx)
