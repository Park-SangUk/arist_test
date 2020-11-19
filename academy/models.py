from django.db import models
from django.urls import reverse

# Create your models here.


class Level(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField('레벨에 대한 설명', max_length=100, blank=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Contents(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=30)
    description = models.CharField(max_length=100, blank=True)
    place = models.CharField('PLACE', max_length=100)
    url = models.URLField('URL')
    start_dt = models.DateTimeField('Start Date')
    end_dt = models.DateTimeField('End Date')
    upload_dt = models.DateTimeField('Upload Date', auto_now_add=True)

    class Meta:
        ordering = ('-upload_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('academy:contents_detail', args=(self.id,))


class Images(models.Model):
    contents = models.ForeignKey(Contents, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="academy/%Y/%m", blank=True, null=True)

    def __str__(self):
        return self.contents.title + " image"
