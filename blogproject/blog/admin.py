from django.contrib import admin

# Register your models here.

from .models import Post, Category, Tag, Helper
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk','title', 'created_time', 'modified_time', 
	 				'category', 'author','is_deleted']
#admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Helper)

#@admin.register(Category)没有class类不能用@方法的！！！！！！
#@admin.register(Tag)
