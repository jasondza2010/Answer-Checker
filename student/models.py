from django.db import models

# Create your models here.


class StudentAnswer(models.Model):
    seat_no = models.CharField(max_length=25, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    q11 = models.CharField(max_length=10000, null=True)
    q12 = models.CharField(max_length=10000, null=True)
    q13 = models.CharField(max_length=10000, null=True)
    q14 = models.CharField(max_length=10000, null=True)
    q21 = models.CharField(max_length=10000, null=True)
    q22 = models.CharField(max_length=10000, null=True)
    q23 = models.CharField(max_length=10000, null=True)
    q24 = models.CharField(max_length=10000, null=True)
    q25 = models.CharField(max_length=10000, null=True)
    q31 = models.CharField(max_length=10000, null=True)
    q32 = models.CharField(max_length=10000, null=True)
    q33 = models.CharField(max_length=10000, null=True)
    q34 = models.CharField(max_length=10000, null=True)
    q35 = models.CharField(max_length=10000, null=True)

    def __str__(self):
        return self.seat_no + '   SUBMITTED AT :  ' + str(self.created_date) + '   MODIFIED AT ' + str(self.modified_date)


class Result(models.Model):
    seat_no = models.CharField(max_length=25, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    q11 = models.CharField(max_length=5, null=True)
    q12 = models.CharField(max_length=5, null=True)
    q13 = models.CharField(max_length=5, null=True)
    q14 = models.CharField(max_length=5, null=True)
    q1_tot = models.CharField(max_length=5, null=True)
    q21 = models.CharField(max_length=5, null=True)
    q22 = models.CharField(max_length=5, null=True)
    q23 = models.CharField(max_length=5, null=True)
    q24 = models.CharField(max_length=5, null=True)
    q25 = models.CharField(max_length=5, null=True)
    q2_tot = models.CharField(max_length=5, null=True)
    q31 = models.CharField(max_length=5, null=True)
    q32 = models.CharField(max_length=5, null=True)
    q33 = models.CharField(max_length=5, null=True)
    q34 = models.CharField(max_length=5, null=True)
    q35 = models.CharField(max_length=5, null=True)
    q3_tot = models.CharField(max_length=5, null=True)
    tot = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.seat_no + '   Total Marks:' + self.tot + '/20   CREATED AT :' + str(self.created_date) + '   MODIFIED AT:' + str(self.modified_date)
