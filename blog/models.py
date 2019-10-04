from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField(max_length = 10000)
    image = models.ImageField(upload_to = 'images/')
    pub_date = models.DateTimeField()


    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:165]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')