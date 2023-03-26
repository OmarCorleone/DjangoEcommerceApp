from django.contrib import admin
from .models import Page,Carousel
# Register your models here.





class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('pk',
                    'title',
                    'slug',
                    'status',
                    'updated_at',
                    # Page/models.py nin içindeki classın fieldlarını yazıyon buraya display edilecek kısım
                    )
    list_filter=("status",)
    list_editable=("status",
                   "title",
                   )


class CarouselAdmin(admin.ModelAdmin):
    list_display=(
        "pk",
        "title",
        "cover_image",
        "status",
        "updated_at"
    )
    list_filter=("status",)
    list_editable=(
        "status",
        "title",

    )
admin.site.register(Page,PageAdmin)
admin.site.register(Carousel,CarouselAdmin)


