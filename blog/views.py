from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
	)
from .models import Post
from .forms import BookForm, RsvpForm, RsvpTemplateForm
from .models import Book, Rsvp, Rsvp_template
# from django.core.mail import send_email
from django.conf import settings

def home(request):	
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


class PostListView(ListView):
	model = Post 
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 10


class UserPostListView(ListView):
	model = Post 
	template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 10

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['address', 'city_state']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostAddNew(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['address', 'city_state']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['address', 'city_state']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url ='/'
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def upload(request):
	context = {}
	if request.method =='POST':
		upload_file = request.FILES['document']
		fs = FilesSystemStorage()
		name = fs.save(uploaded_file.name, upload_file)
		context['url'] = fs.url(name)
	return render(request, 'upload.html', context)

def book_list(request):
	books = Book.objects.all()
	return render(request, 'blog/book_list.html', { 'books': books })

def upload_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('blog-book_list')
	else:
		form = BookForm()
	return render(request, 'blog/upload_book.html', { 'form': form})

def rsvp_list(request):
	rsvps = Rsvp.objects.all()
	return render(request, 'blog/rsvp_list.html', { 'rsvps': rsvps })

def upload_rsvp(request):
	if request.method == 'POST':
		form = RsvpForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('blog-rsvp_list')
	else:
		form = RsvpForm()
	return render(request, 'blog/upload_rsvp.html', { 'form': form})

def delete_rsvp(request, pk):
	if request.method == 'POST':
		rsvp = Rsvp.objects.get(pk=pk)
		rsvp.delete()
	return redirect('blog-rsvp_list')	

def delete_book(request, pk):
	if request.method == 'POST':
		book = Book.objects.get(pk=pk)
		book.delete()
	return redirect('blog-book_list')

def rsvp_template(request):
	if request.method == 'POST':
		form = RsvpTemplateForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('blog-rsvp_template')
	else:
		form = RsvpTemplateForm()
	return render(request, 'blog/rsvp_template.html', { 'form': form})

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def acquisition(request):
	return render(request, 'blog/acquisition.html', {'title': 'About'})

def index(request):

	if request.method == 'POST':
		message = request.POST['message']
		send_mail('You have been invited!',
			message,
			settings.EMAIL_HOST_USER,
			['kathao63@yahoo.com'],
			fail_silently=False)
	return render(request, 'blog/index.html')
