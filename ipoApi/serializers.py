# ipo_data/serializers.py

from rest_framework import serializers
from .models import IPO

class IPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPO
        fields = [
            'company_name',
            'price_band',
            'open_date',
            'close_date',
            'issue_size',
            'issue_type',
            'listing_date',
            'listing_date_2',  # Added field
            'status',
            'ipo_price',
            'listing_price',
            'listing_gain',
            'current_market_price',
            'current_return',
            'rhp_url',
            'drhp_url',
            'company_logo'
        ]
