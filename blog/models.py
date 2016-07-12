from django.db import models
from django.utils import timezone
from redactor.fields import RedactorField

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    text = RedactorField(
        verbose_name=u'Text',
        redactor_options={'lang': 'en', 'focus': 'true'},
        upload_to='tmp/',
        allow_file_upload=True,
        allow_image_upload=True
)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
