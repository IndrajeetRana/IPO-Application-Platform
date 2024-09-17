# ipo_data/models.py

from django.db import models

class IPO(models.Model):
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    company_name = models.CharField(max_length=255)
    price_band = models.CharField(max_length=50)
    open_date = models.DateField()
    close_date = models.DateField()
    issue_size = models.CharField(max_length=50)
    issue_type = models.CharField(max_length=50)
    listing_date = models.DateField(null=True, blank=True)
    listing_date_2 = models.DateField(null=True, blank=True)  # Added field
    status = models.CharField(max_length=50)
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    listing_gain = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_market_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_return = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rhp_url = models.URLField(max_length=500, null=True, blank=True)
    drhp_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.company_name
