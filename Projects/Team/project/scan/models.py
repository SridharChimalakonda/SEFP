from __future__ import unicode_literals

from django.db import models

# Create your models here.
"""
class quickScan(models.Model):
    scan_id = models.AutoField(primary_key=True)        #Not the UUID, this ID is for DB only
    scan_uuid = models.CharField(max_length=40)
    scan_date = models.DateTimeField(editable=False)
    scan_url = models.URLField(max_length=200)
    scan_status = models.CharField(max_length=7)
    scan_results = models.TextField(max_length=5000, default="")"""

class payLoads(models.Model):
	"""This table will consist of a database of a payload"""
	payload = models.CharField(max_length=1000)
	vulnerability = models.TextField(max_length=50)

class fingerPrints(models.Model):
	"""This table will consist of various fingerprints of a server"""
	fingerPrint = models.CharField(max_length=1000)
	vulnerability = models.TextField(max_length=50)
		