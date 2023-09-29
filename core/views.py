from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# List View : works on multiple object and list them out
# Detail View: works on single object and display only the object
# Create View: Creates an object
# Update View: Updates an object
# Delete View: Deletes an object

# Create your views here.

# def home(request):
#     return render(request, "home.html",{})

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    #ordering = ['-id']  #This makes objects order like a stack i.e old one goes to last. Default ordereing is like queue
    ordering =['-date']
    
    # For sending context to a page
    def get_context_data(self, *args,**kwargs):
        cats_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context["cats_menu"] = cats_menu
        return context

class ArticleView(DetailView):
    model = Post
    template_name="article.html"
    
    def get_context_data(self, *args,**kwargs):
        cats_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(*args,**kwargs)
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = bool(stuff.likes.filter(id=self.request.user.id).exists())
        context["cats_menu"] = cats_menu
        context["toatl_likes"] = total_likes
        context["liked"] = liked
        return context
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm # Adding from forms.py, no need to define fields now, because it's being taken care of by the forms  # noqa: E501
    template_name = "add_post.html"
    #fields = '__all__'  # This will get every fields of Post model
    #fields=('title', 'body') # this will only get title and body field of Post model

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "update_post.html"
    #fields = ('title','body')  # You can't have both field and form_class

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home') # After deleting object where to go
    
    
class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = "add_category.html"

# Try to add "update Category view"


def categoryView(request,cats):
    # cats are the second part of the dynamic url in the urls.py file of core. The <str:cat> part
    cats = cats.replace("-"," ")  # The replace part is for slugify
    category_posts = Post.objects.filter(category = cats)  # This is making a query like -> select * from Post where category=cats; 
    
    # objects isn't callable (is an attribute).
    # Talk.objects() --> won't work
    # Talk.objects --> will work
    
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})  # title() is for I guess capitalizing the first letter

def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))  # "get_object_or_404" is for get the post from the Post table if like for it is inputed or return 404 error # "post_id" is because we named our like button post_id
    
    if post.likes.filter(id=request.user.id).exists(): # if the user already click the button, clicking it again will remove the like
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user) # not only we are saving the like but also who likes the post
    
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))