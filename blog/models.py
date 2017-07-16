from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse

class Category(models.Model):

	category_title = models.CharField(verbose_name = 'Category Title', max_length = 250)

	category_image = models.ImageField(upload_to = 'category_images/%Y/%m/%d')

	category_description = RichTextField()

	slug = models.SlugField(max_length = 250, unique = True)

	date_created = models.DateTimeField(auto_now_add = True)


	def __str__(self):

		return self.category_title

	def get_absolute_url(self):

		return reverse("blog:category-content", kwargs = {"slug": self.slug})



class Post(models.Model):

	title = models.CharField(verbose_name = "Blog Title", max_length = 250)

	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	body = RichTextField()

	date_posted = models.DateTimeField(auto_now_add = True)

	featured_image = models.ImageField(upload_to = 'featured_images/%Y/%m/%d')

	user = models.ForeignKey(User, on_delete = models.CASCADE)

	slug = models.SlugField(max_length = 250, unique = True)


	def __str__(self):

		return reverse("blog:post-content", kwargs = {"slug": self.slug})

	


