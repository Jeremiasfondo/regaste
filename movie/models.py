from django.db import models

# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {} ".format(self.title, self.description)

class moviedb(models.Model):
    title = models.CharField(max_length=255, null=False)
    minutes = models.CharField(max_length=255, null=False)
    release_date  = models.DateField()
    main_actor = models.CharField(max_length=255, null=False)
    productor = models.CharField(max_length=255, null=False)
    picture = models.ImageField(upload_to = 'templates/images/movie/')
    url = models.URLField(max_length=225)
    price = models.CharField(max_length=255, null=False)
    description = models.TextField()
    category   =  models.ForeignKey(category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}  -  {}".format(self.title, self.release_date, self.category)


class trailer(models.Model):
    title = models.CharField(max_length=255, null=False)
    url = models.URLField(max_length=225)
    movie_id   =  models.ForeignKey(moviedb, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class payment(models.Model):
    movie_id    =  models.ForeignKey(moviedb, on_delete=models.CASCADE)
    status = models.BooleanField() 
    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


