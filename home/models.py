from django.db import models


class contact_form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'Name: {self.first_name, self.last_name} | Email: {self.email} | Date: {self.date} | Notes: {self.notes}'