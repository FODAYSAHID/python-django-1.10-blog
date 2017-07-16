from django.contrib import admin
from blog.models import Category, Post

class CategoryAdmin(admin.ModelAdmin):

	list_display = ('category_title', 'category_description', 'date_created', 'slug')

	search_fields = ['category_title']

	prepopulated_fields = {"slug": ('category_title',)}



class PostAdmin(admin.ModelAdmin):

	list_display = ('title', 'category', 'date_posted')

	search_fields = ['title']

	prepopulated_fields = {"slug": ('title',)}



admin.site.site_header = "Foday's Blog"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
