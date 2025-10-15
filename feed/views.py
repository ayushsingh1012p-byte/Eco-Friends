from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, PostForm, ProductForm, UserProfileForm
from .models import Post, Product, UserProfile
from django.contrib.auth.models import User

@login_required
def feed_view(request):
    posts = Post.objects.all().order_by('-created_at')
    profile = UserProfile.objects.get(user=request.user)
    profile.update_rank()
    profile.save()

    query = request.GET.get('q', '').strip()
    users = User.objects.none()  # default empty queryset

    if query:
        users = User.objects.filter(username__icontains=query)

    return render(request, 'home.html', {
        'posts': posts,
        'profile': profile,
        'users': users,
        'query': query
    })

@login_required
def store_view(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'store.html', {'products': products})

def signup_view(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = SignupForm()
        profile_form = UserProfileForm()

    return render(request, 'signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def upload_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def upload_product_view(request):
    if request.method == 'POST':
        form  = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('store')
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})


@login_required
@csrf_exempt
def post_likes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'likes_count': post.likes.count()
    })

@login_required
def get_liked_users(request, pk):
    post = get_object_or_404(Post, pk=pk)
    users = post.likes.all().values('username', 'id')
    return JsonResponse(list(users), safe=False)

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = UserProfile.objects.get(user=user)
    posts = Post.objects.filter(user=user).order_by('-created_at')
    return render(request, 'profile.html', {'profile': profile, 'posts': posts})




    

