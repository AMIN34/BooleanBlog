from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Author is coming from the Django admin panel and on_delete means every thing under that author will be delete in one swoop  # noqa: E501
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    category = models.CharField(max_length=255, default="uncategorized")
    date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')  # This allows us to associate different things to different table such as many users may like many posts 
    # "related_name" acts like a foreign key, it associates many things with each other
    header_image = models.ImageField(null=True, blank=True, upload_to="images/") # null and blank are for the purpose that a blog may not have an image and that's ok and if there isn't one, one can be added later
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self) -> str:
        return f"{self.title} || {str(self.author)}"
    
    #  It's like a magic button that gives us the full URL for any page we want, just by using the page's name
    def get_absolute_url(self):
        #return reverse("article", kwargs={"pk": self.pk})
        return reverse("home")
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    #  It's like a magic button that gives us the full URL for any page we want, just by using the page's name
    def get_absolute_url(self):
        #return reverse("article", kwargs={"pk": self.pk})
        return reverse("home")
    
    class Meta:
        # Django automatically pluralizes a model name by adding a 's' to the model name. So to make it your own convention use this Meta... function? attributes?... I don't know but use this when needed
        verbose_name_plural = "Categories"
    