from django.db import models


class UserAccount(models.Model):
    username = models.CharField(max_length=50, unique=True)
    mail = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.username} - {self.age}"


class BloodPressure(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.systolic} / {self.diastolic} mm Hg"
