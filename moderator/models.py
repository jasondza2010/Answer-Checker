from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Question(models.Model):
    q = models.CharField(max_length=25)
    question = models.CharField(max_length=1000)
    prev_ppr = models.CharField(max_length=25, blank=True, null=True)
    options = models.CharField(max_length=500, blank=True, null=True)
    answer = models.CharField(max_length=5000)
    c_ky = models.CharField(max_length=500, blank=True, null=True)
    v_ky = models.CharField(max_length=500, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('moderator:index')

    def __str__(self):
        return self.q+' '+self.question


class QuestionPaper(models.Model):
    moderator_name = models.CharField(max_length=25, null=True, default='jd_gourea')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    q11 = models.CharField(max_length=25)
    q12 = models.CharField(max_length=25)
    q13 = models.CharField(max_length=25)
    q14 = models.CharField(max_length=25)
    q21 = models.CharField(max_length=25)
    q22 = models.CharField(max_length=25)
    q23 = models.CharField(max_length=25)
    q24 = models.CharField(max_length=25)
    q25 = models.CharField(max_length=25)
    q31 = models.CharField(max_length=25)
    q32 = models.CharField(max_length=25)
    q33 = models.CharField(max_length=25)
    q34 = models.CharField(max_length=25)
    q35 = models.CharField(max_length=25)

    def __str__(self):
        return self.moderator_name + '  CREATED AT :  ' + str(self.created_date) + '  MODIFIED AT ' + str(self.modified_date)
