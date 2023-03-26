from django.contrib import admin
from .models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('pk',
                    'title',
                    'slug',
                    'gender',
                    'status',
                    'updated_at',
                    # product/models.py nin içindeki classın fieldlarını yazıyon buraya display edilecek kısım
                    )
    list_filter=("status",
                 'gender',
                 )
    list_editable=("status",
                   "title",
                   )


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('pk',
                    'title',
                    'price',
                    'stock',
                    'slug',
                    'status',
                    'updated_at',
                    # product/models.py nin içindeki classın fieldlarını yazıyon buraya display edilecek kısım
                    )
    list_filter=("status",)
    list_editable=("status",
                   "title",
                   )
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
