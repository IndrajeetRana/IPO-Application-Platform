import requests
from django.shortcuts import render

def ipo(request):
    return render(request, 'index.html')

def upcomming(request):
    # Define static IPO data
    static_ipos = [
        {
            'name': 'Company A',
            'price_band': 'Rs 100 - 120',
            'open_date': '2024-01-22',
            'close_date': '2024-01-24',
            'issue_size': '143.81 Cr',
            'issue_type': 'Book Built',
            'listing_date': '2024-01-30',
          # Add the path to the company logo
        },
        {
            'name': 'Company B',
            'price_band': 'Rs 200 - 220',
            'open_date': '2024-02-15',
            'close_date': '2024-02-17',
            'issue_size': '200 Cr',
            'issue_type': 'Fixed Price',
            'listing_date': '2024-02-25',
          # Add the path to the company logo
        },
        {
            'name': 'Company C',
            'price_band': 'Rs 300 - 320',
            'open_date': '2024-03-01',
            'close_date': '2024-03-03',
            'issue_size': '500 Cr',
            'issue_type': 'Book Built',
            'listing_date': '2024-03-10',
          # Add the path to the company logo
        },
        {
            'name': 'Company D',
            'price_band': 'Rs 400 - 420',
            'open_date': '2024-04-15',
            'close_date': '2024-04-17',
            'issue_size': '1000 Cr',
            'issue_type': 'Fixed Price',
            'listing_date': '2024-04-25',
          # Add the path to the company logo
        },
        {
            'name': 'Company E',
            'price_band': 'Rs 500 - 520',
            'open_date': '2024-05-01',
            'close_date': '2024-05-03',
            'issue_size': '200 Cr',
            'issue_type': 'Book Built',
            'listing_date': '2024-05-10',
          # Add the path to the company logo
        }
    ]

    # Fetch IPO data from the API
    api_url = 'http://127.0.0.1:8000/api/ipos/'  # Your API endpoint
    response = requests.get(api_url)
    
    if response.status_code == 200:
        # Parse the JSON response
        all_ipos = response.json()
        # Filter upcoming IPOs
        upcoming_ipos = [
            ipo for ipo in all_ipos
            if ipo['listing_date'] > '2024-08-29'  # Adjust the date comparison as needed
        ]
    else:
        # Handle API request failure
        upcoming_ipos = []

    # Combine static data with API data
    combined_ipos = static_ipos + upcoming_ipos

    return render(request, 'upcomming.html', {'upcoming_ipos': combined_ipos})