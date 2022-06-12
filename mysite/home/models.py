from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=256, unique=True, null=False)
    about = models.TextField(max_length=500, null=False)
    content = models.TextField(max_length=1024, null=False)
    author = models.CharField(max_length=100, null=False)
    image = models.FileField(null=False, upload_to='news/')
    published = models.DateTimeField(null=False, auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return str(self.title) + ' -> ' + str(self.about) + ' / ' + str(self.published)

