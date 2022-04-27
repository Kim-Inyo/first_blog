from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class HomeView(ListView):
    model = Post
    ordering = ['-created']
    template_name = 'users/home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'users/articledetail.html'

class AddPostView(CreateView):
    model = Post
    fields = ['title', 'body']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    template_name = 'users/post-creation.html'

def home(request):
    return render(request, 'users/home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home')
    return render(request, 'users/signup.html', {'form':form})

def post_create(request):
        
    return render(request, 'users/post-creation.html')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        name = request.GET.get('username')
        password = request.GET.get('password')
        user = authenticate(request, username = name, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html')

def logoutpage(request):
    logout(request)
    return redirect('home')

def profile(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'users/profile.html')

def friends(request):
    return render(request, 'users/friends.html')

# Create your views here.
