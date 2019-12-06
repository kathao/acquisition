from django.shortcuts import render
from .models import Images
from django.forms import modelformset_factory
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

class Home(TemplateView):
	template_name = 'home.html'

def upload(request):
	# context = {}
	# if request.method =='POST':
	# 	upload_file = request.FILES['document']
	# 	fs = FilesSystemStorage()
	# 	name = fs.save(uploaded_file.name, upload_file)
	# 	context['url'] = fs.url(name)
	return render(request, 'upload.html', context)

def book_list(request):
	return render(request, 'book_list.html')

def upload_book(request):
		return render(request, 'upload_book.html')
