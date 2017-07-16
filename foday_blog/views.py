from django.shortcuts import render


def custom_404(request):

	return render(request, 'error_pages/404.html')


def custom_500(request):

	return render(request, 'error_pages/500.html')