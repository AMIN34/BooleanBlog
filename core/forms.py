from django import forms
from .models import Post, Category

# Hard coding choices
#choices = [('uncategorized','uncategorized'),('sports','sports'),('coding','coding')]   
#These are slug boxes, and it is a list of tuples containing the same thing, one for remembering it and other is actual thing

#Pulling choices from a model
choices =list(Category.objects.all().values_list('name','name'))  # Model query... selecting everything in the table 
# Without giving any parameter to values_list it worked fine but I think its because Category model has only one field "name" and yes 'name' in values_list because our field name in the model is "name".

# The values() method returns a QuerySet containing dictionaries: <QuerySet [{'comment_id': 1}, {'comment_id': 2}]>
# The values_list() method returns a QuerySet containing tuples: <QuerySet [(1,), (2,)]>

class PostForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = ("title","author","category","body","header_image") # What fields will be there in the site in the form


        # attrs -> its like attributes of html tags, keys are the atribute name and value are the required value needed for the attributes   # noqa: E501
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title here'}),  # noqa: E501
            'category': forms.Select(choices=choices, attrs={'class':'form-control'}),  # You have to write choices before attrs otherwise it will show error
            #'author': forms.Select(attrs={'class':'form-control','value':'', 'id':'author_id'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'author_id', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","body")


        # attrs -> its like attributes of html tags, keys are the atribute name and value are the required value needed for the attributes   # noqa: E501
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title here'}),  # noqa: E501
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }