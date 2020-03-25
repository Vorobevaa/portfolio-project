from django.db import models

# Create Blog models
# title
# pub_date
# body
# image


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")

# Add to the admin

