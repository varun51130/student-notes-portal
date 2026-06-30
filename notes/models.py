from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,
            null=True,blank=True)
    title = models.CharField(max_length=200)

    subject = models.CharField(max_length=100)

    semester = models.IntegerField()

    description = models.TextField()

    pdf = models.FileField(
    upload_to='notes_pdfs/',
    blank=True,
    null=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title