from django.db import models



class Projects(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    
    def __str__(self):
        return self.name


class Image(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_image/')





















