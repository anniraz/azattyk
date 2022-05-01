from django.contrib import admin

# Register your models here.
from news.models import News, Category
class NewsAdmin(admin.ModelAdmin):
    list_display=['title','category']
    prepopulated_fields={'url':('title',)}

admin.site.register(News,NewsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','url']
    prepopulated_fields={'url':('name',)}

admin.site.register(Category,CategoryAdmin)
