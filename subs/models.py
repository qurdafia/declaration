from django.db import models
from django.utils import timezone
import datetime


class Sub(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    date_format = '%d-%m-%Y %H:%M:%S'

    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255, default='')
    company = models.CharField(max_length=255, default='')
    purpose = models.TextField(default='')
    temperature = models.CharField(max_length=255, default='')
    time_scanned = models.CharField(max_length=255, default='', blank=False)
    visit_pass_number = models.CharField(max_length=255, default='')

    is_quarantined = models.BooleanField(choices=BOOL_CHOICES, default=False)
    is_contacted = models.BooleanField(choices=BOOL_CHOICES, default=False)
    has_travelled = models.BooleanField(choices=BOOL_CHOICES, default=False)
    is_unwell = models.BooleanField(choices=BOOL_CHOICES, default=False)

    reg_date = models.DateField(default=timezone.now)
    acknowledge = models.BooleanField(choices=BOOL_CHOICES, default=True)

    def get_full_name(self):
        """Get full name of the user"""
        return self.name

    def get_short_name(self):
        """Get short name of the user"""
        return self.name

    def __str__(self):
        """Render string in the admin"""
        return self.name + ' - ' + self.mobile_number
