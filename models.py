Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from django.db import models
... 
... class Patient(models.Model):
...     patient_id = models.AutoField(primary_key=True)
...     patient_name = models.CharField(max_length=100)
...     age = models.IntegerField()
...     problem_desc = models.TextField()
...     profile_date = models.DateTimeField()
...     access_data = models.CharField(max_length=200)
...     gender = models.CharField(max_length=20)
...     contact_no = models.CharField(max_length=20)
...     address = models.TextField()
...     blockchain_hash = models.CharField(max_length=256)
