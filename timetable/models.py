from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.



class state(models.Model):
    state_name=models.CharField(max_length=60)

    def __str__(self):
        return self.state_name

class campus(models.Model):
    state=models.ForeignKey(state, on_delete=models.CASCADE)
    campus_name=models.CharField(max_length=60)
    campus_email=models.EmailField(max_length=30)
    campus_phone=models.CharField(max_length=60)
    campus_address=models.CharField(max_length=100)
    campus_manager=models.CharField(max_length=60)


    def __str__(self):
        return self.campus_name

USAGE_RECOMMENDATION = {
        ("CURRENT", "CURRENT"),
        ("SUPERSESEDED", "SUPERSESEDED"),
       }

TERM = {
        ("Semester 1 Term 1", "Semester 1 Term 1"),
        ("Semester 1 Term 2", "Semester 1 Term 2"),
        ("Semester 2 Term 1", "Semester 2 Term 1"),
        ("Semester 2 Term 2", "Semester 2 Term 2"),
        ("Semester 3 Term 1", "Semester 3 Term 1"),
        ("Semester 3 Term 2", "Semester 3 Term 2"),
        ("Semester 4 Term 1", "Semester 4 Term 1"),
        ("Semester 4 Term 2", "Semester 4 Term 2"),

       }

class Qualification(models.Model):
    national_code = models.CharField(max_length=10)
    qualification_name = models.CharField(max_length=60)
    usage_recommendation = models.CharField(max_length=50, choices=USAGE_RECOMMENDATION)
    total_duration = models.IntegerField()
    total_core_units = models.IntegerField()
    total_elective_units = models.IntegerField()
    total_units = models.IntegerField()
    term = models.CharField(max_length=100, choices=TERM)
    start_date=models.DateField()
    proposed=models.DateField()
    intake_date=models.DateField()





    def __str__(self):

        return self.national_code
        return self.qualification_name




STATUS = {
        ("CORE", "CORE"),
        ("ELECTIVE", "ELECTIVE"),
       }







class Units(models.Model):
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, null=True,  related_name='Qualification.national_code +' )
    unit_code = models.CharField(max_length=15)
    unit_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS)
    duration = models.IntegerField()



    def __str__(self):
        return self.unit_name





class Break(models.Model):
    weeks = models.IntegerField()
    title = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
         return self.title





