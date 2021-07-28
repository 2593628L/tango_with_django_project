from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    return render(request,'rango/index.html',context=context_dict)



def about(request):
    return render(request,'rango/about.html')

def show_category(request,category_name_slug):
    context_dic={}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dic['pages'] = pages
        print(pages)
        context_dic['category'] = category
    except Category.DoesNotExist:
        context_dic['category'] = None
        context_dic['pages'] = None
        

    return render(request,'rango/category.html',context=context_dic)

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/')
        else:
            print(form.error)
    return render(request,'rango/add_category.html',{'form':form})
    