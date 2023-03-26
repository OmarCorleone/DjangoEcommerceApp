from django.db import models
from page.models import DEFAULT_STATUS,STATUS

GENDER_CHOICE=[
            ('man','Erkek'),
            ('woman','Kadın'),
            ('unisex','Unisex'),
        ]

#Category

class Category(models.Model):
    #title 
    title=models.CharField(max_length=200)
    #slug sadece create de oluşturacan
    slug=models.SlugField(max_length=200,default="")
    #status
    status=models.CharField(default=DEFAULT_STATUS,choices=STATUS,max_length=10)
    #created_at
    created_at=models.DateTimeField(auto_now_add=True)
    #updated_at
    updated_at=models.DateTimeField(auto_now=True)
    gender=models.CharField(
        max_length=6,
        default="unisex",
        choices=GENDER_CHOICE,
                            )
    is_men=models.BooleanField(default=False)
    is_women=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.pk}-{self.gender}-{self.title}'


#Product

class Product(models.Model):
    category=models.ForeignKey(Category,
                               on_delete=models.CASCADE
                               )
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,default="")
    content=models.TextField()
    cover_image = models.ImageField(upload_to='page',null=True,blank=True)
    status=models.CharField(default=DEFAULT_STATUS,choices=STATUS,max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    stock=models.PositiveIntegerField(default=0) 
    price=models.FloatField()


