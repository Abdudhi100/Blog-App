from django.db import models

# Create your models here.
from django.db import models #we are telling django to import the models attributes from db
from django.utils.timezone import now #we are telling djago to get the attribute we can use to deduce present date from its util.timezone methods


class Post(models.Model): #this is a form field class that creates a database for the app. It goes into models.Model for its functionalities
    title = models.CharField(max_length=200) #this create the title field column in the database to save the blog post titles
    content = models.TextField() # this creates the blog content body column
    created_at = models.DateTimeField(default=now) #this creates a column that saves the date the post was created
    updated_at = models.DateTimeField(auto_now=True) # this createes a column that saves the time the blog post was last edited
    
    def _str_(self):
        return self.title #this method defines how the object will be defined as a string, and when the object is being referenced, it will return the title 
    