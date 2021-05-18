from django.shortcuts import render

# Create your views here.

def home_page_view(request):
	return render(request, 'website/home.html')

def multimedia_page_view(request):
	return render(request, 'website/multimedia.html')

def about_page_view(request):
	return render(request, 'website/about.html')