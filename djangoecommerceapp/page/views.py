from django.shortcuts import render ,redirect
from django.contrib import messages
from .models import Carousel,Page
from .forms import CarouselModelForm,PageModelForm
from django.utils.text import slugify
from django.contrib.admin.views.decorators import staff_member_required
from product.models import Category
STATUS='published'
# Create your views here.

# User viewing this:
def index(request):
    
    images=Carousel.objects.filter(status="published"
                                   
    ).exclude(cover_image='')
     
    
    context={
        "images":images,
        # 'categories':Category.objects.filter(
        # status=STATUS
        # ).order_by('title'),
    }

    return render(request,"home/index.html",context)


# Admin:
def carousel_create(request):
    context={}
    context['title']="Carousel Create Form"
    context['form']=CarouselModelForm()
    # item=Carousel.objects.first()
    # context['form']=CarouselModelForm(instance=item)
    if request.method=='POST':
        # create code is deleted 
        form = CarouselModelForm(data=request.POST,files=request.FILES)
        
        if form.is_valid():
            form.save()
        messages.success(request,"Başarıyla eklendi ! ")
    return render(request,"manage/form.html",context)

@staff_member_required
def page_list(request):
    context={}
    context['items']=Page.objects.all().order_by('-pk')
    return render(request,"manage/page_list.html",context)


def page_create(request):
    context={}
    context['title']="Page Create Form"
    context['form']=PageModelForm()
    # item=Carousel.objects.first()
    # context['form']=CarouselModelForm(instance=item)
    if request.method=='POST':
        # create code is deleted 
        form = PageModelForm(data=request.POST,files=request.FILES)
        
        if form.is_valid():
            item=form.save(commit=False)
            item.slug=slugify(item.title.replace('ı','i'))

            item.save()

        messages.success(request,"Başarıyla eklendi ! ")
    return render(request,"manage/form.html",context)


def page_update(request,pk): #pk vermezsen gelmez
    context={}
    item=Page.objects.get(pk=pk)
    context['title']=f"Title : {item.title } - Pk : {item.pk} Page Update Form"
    context['form']=PageModelForm(instance=item)
    if request.method=="POST":
        context['form']=PageModelForm(instance=item,data=request.POST,files=request.FILES)
        if context['form'].is_valid():
            item= context['form'].save(commit=False)
            if item.slug=='':
                item.slug=slugify(item.title.replace('ı','i'))
            item.save()
            messages.success(request,'Guncellendi!')
            return redirect('page_update',pk)
    return render(request,"manage/form.html",context)

def carousel_delete(request,pk):
    item=Carousel.objects.get(pk=pk)
    item.status='deleted'
    item.save()
    return redirect('carousel_list')


def page_delete(request,pk):
    item=Page.objects.get(pk=pk)
    item.status='deleted'
    item.save()
    return redirect('page_list')


def carousel_list(request):
    context={}
    context['carousel']=Carousel.objects.all().order_by('-pk')
    return render(request,"manage/carousel_list.html",context)


def carousel_update(request,pk): #pk vermezsen gelmez
    context={}
    item=Carousel.objects.get(pk=pk)
    context['title']=f"Title : {item.title } - Pk : {item.pk} Carousel Update Form"
    context['form']=CarouselModelForm(instance=item)
    if request.method=="POST":
        context['form']=CarouselModelForm(instance=item,data=request.POST,files=request.FILES)
        if context['form'].is_valid():
            context['form'].save()
            messages.success(request,'Guncellendi!')
            return redirect('carousel_update',pk)
    return render(request,"manage/form.html",context)

def manage_list(request):
    context={}
    return render(request,'manage/manage.html',context)



