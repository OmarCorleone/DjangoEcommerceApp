from django.db import models

DEFAULT_STATUS="draft"
# Status tuples şeklinde olmalı [(db de gözüken kısım,admin panelde gözüken kısım),(),()]
STATUS=[
    ("draft","Taslak"),
    ("published","Yayınlandı"),
    ("deleted","Silindi"),
]

class Page(models.Model):
    #title 
    title=models.CharField(max_length=200)
    #slug sadece create de oluşturacan
    slug=models.SlugField(max_length=200,default="")

    #content
    content=models.TextField()

    #cover_image
    cover_image = models.ImageField(upload_to='page',null=True,blank=True)
    #status
    status=models.CharField(default=DEFAULT_STATUS,choices=STATUS,max_length=10)
    #created_at
    created_at=models.DateTimeField(auto_now_add=True)
    #updated_at
    updated_at=models.DateTimeField(auto_now=True)


class Carousel(models.Model):
    #title
    title=models.CharField(max_length=200,null=True,blank=True)
    #image
    cover_image = models.ImageField(upload_to='carousel',
                                    null=True,
                                    blank=True,
                                    )
    #status
    status=models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )
    #created_at
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    #updated_at
    updated_at=models.DateField(auto_now=True,null=True,blank=True)



