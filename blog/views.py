from django.shortcuts import render
from blog.models import Category, Post
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def index(request):

	query = Category.objects.all().order_by('-date_created')[:12]

	return render(request, 'blog/categories.html', {'query': query})

def categoryContent(request, slug):

	query = Category.objects.get(slug = slug)

	posts = query.post_set.all().order_by('-date_posted')[:20]

	return render(request, 'blog/category_list.html', {"posts": posts, "query":query})


def postContent(request, slug):

	post = Post.objects.get(slug = slug)

	related_post = Post.objects.all().order_by("-date_posted")[:10]

	return render(request, 'blog/post_content.html', {"post": post, "related_post": related_post})


def contactMe(request):

	if request.method == "POST":

		form = ContactForm(request.POST)

		if form.is_valid():

			full_name = form.cleaned_data['full_name']

			email = form.cleaned_data['email']

			subject = form.cleaned_data['subject']

			message = form.cleaned_data['message']

			message = full_name + "\n\n" + message 

			receipient = [email, "@gmail.com"]

			send_mail(subject, message, email, receipient)

			return HttpResponseRedirect("/thanks-for-contacting-me/")


	else:

		form = ContactForm()

	return render(request, "blog/contact.html", {"form": form})


def blogPost(request):

	query = Post.objects.all().order_by("-date_posted")

	return render(request, "blog/blog_list.html", {"query": query})


def mailOnSuccess(request):

	return render(request, "blog/thanks.html")


def aboutMe(request):

	return render(request, "blog/about.html")
