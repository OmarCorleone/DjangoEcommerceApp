from django import forms
from .models import Carousel,Page

class CarouselModelForm(forms.ModelForm):
    class Meta:
        model=Carousel
        # fields= '__all__' do not use this 
        fields=["title",
                 "cover_image",
                 'status',

                 ]


class PageModelForm(forms.ModelForm):
    class Meta:
        model = Page

        # exclude=["title"] dont use this 
        fields=[
            'title',
            'cover_image',
            'content',
            'status',

        ]