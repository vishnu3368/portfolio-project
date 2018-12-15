from django.db import models

# Create A Blog models

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    # title
    pub_date = models.DateTimeField()
    #publication_date
    body = models.TextField()
    #body
    image = models.ImageField(upload_to='images/')
    #image

# Add the blog app to the settings
# Create a migration
# migrate
# add to the admin
