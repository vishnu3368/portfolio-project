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
    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):

        return self.title

    





# Add the blog app to the settings
# Create a migration
# migrate
# add to the admin
