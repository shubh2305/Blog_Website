from django.shortcuts import render, redirect, reverse
from django.http import Http404
from .forms import NewUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Profile, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
# def home(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts
#     }
#     return render(request, 'index.html', context)

class PostListView(ListView):
    model=Post
    template_name='index.html'
    context_object_name='posts'
    ordering=['-date_created']

class PostDetailView(LoginRequiredMixin, DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title', 'body']
    success_url='/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title', 'body']
    success_url='/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=User
    fields=['username', 'first_name', 'last_name']
    success_url='/'

    def test_func(self):
        x = self.request.user.id
        y = self.kwargs['pk']
        if x == y:
            return True
        else:
            if self.request.user.is_authenticated:
                raise Http404("You are not authenticated to edit this profile")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super(UserUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data["profile"] = ProfileForm(self.request.POST)
        else:
            # accessing the profile object
            data["profile"] = ProfileForm(instance=self.object.profile)
            #data["profile"].save()
        return data
    

def register_view(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, 'Thank You for joining {username}!')
            return redirect('home')
    else:
        form = NewUserForm()
    return render(request, 'blog/register.html', {'form':form})

def profile_view(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'blog/profile_view.html', { 'user':user })

class ProfileCreateView(LoginRequiredMixin, CreateView):
    model=Profile
    fields=['image', 'description']
    success_url='/'

    def form_valid(self):
        form.instance.user = self.request.user

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields=('body',)

    def get_success_url(self):
           pk = self.kwargs["pk"]
           return reverse("post_detail", kwargs={"pk": pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        post_id= self.kwargs['pk']
        form.instance.post = Post.objects.get(pk=post_id)
        return super().form_valid(form)
