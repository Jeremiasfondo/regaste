from django.db import models

# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {} ".format(self.title, self.description)



class movie(models.Model):
    title = models.CharField(max_length=255, null=False)
    minutes = models.CharField(max_length=255, null=False)
    year = models.DateField()
    main_actor = models.CharField(max_length=255, null=False)
    productor = models.CharField(max_length=255, null=False)
    description = models.TextField()
    category   =  models.ForeignKey(category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}  -  {}".format(self.title, self.year, self.category)



