import requests
from django.shortcuts import render
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse


@login_required(login_url='home:signin')
def adminPage(request):
    print("admin page" , request.user)
    user = request.user  # Get the current authenticated user
    context = {
        'username': user.username.upper(),
        'email': user.email,
    }
    
    print(context)
    return render(request, 'base/adminPage.html', context)



def register(request):
    if request.method == 'POST':
        # Extract form data
        company_name = request.POST.get('companyName')
        price_band = request.POST.get('priceBand')
        open_date = request.POST.get('open')
        close_date = request.POST.get('close')
        issue_size = request.POST.get('issueSize')
        issue_type = request.POST.get('issueType')
        listing_date = request.POST.get('listingDate')
        listing_date_2 = request.POST.get('listingDate2')  # Added field
        status = request.POST.get('status')
        ipo_price = request.POST.get('ipoPrice')
        listing_price = request.POST.get('listingPrice')
        listing_gain = request.POST.get('listingGain')
        current_market_price = request.POST.get('cmp')
        current_return = request.POST.get('currentReturn')
        rhp_url = request.POST.get('rhp')
        drhp_url = request.POST.get('drhp')
        company_logo = request.FILES.get('companyLogo')  # Get uploaded file

        # Prepare the data to send to the API
        data = {
            'company_name': company_name,
            'price_band': price_band,
            'open_date': open_date,
            'close_date': close_date,
            'issue_size': issue_size,
            'issue_type': issue_type,
            'listing_date': listing_date,
            'listing_date_2': listing_date_2,  # Added field
            'status': status,
            'ipo_price': ipo_price,
            'listing_price': listing_price,
            'listing_gain': listing_gain,
            'current_market_price': current_market_price,
            'current_return': current_return,
            'rhp_url': rhp_url,
            'drhp_url': drhp_url,
        }

        files = {
            'company_logo': company_logo,
        }

        # Debug information
        print("Data:", data)
        print("Files:", files)

        # Call your external API
        api_url = 'http://127.0.0.1:8000/api/ipos/'  # Replace with your actual API URL
        response = requests.post(api_url, data=data, files=files)

        print("Response Status Code:", response.status_code)
        print("Response Content:", response.content)

        if response.status_code == 201:  # 201 Created is a typical success status for POST requests
            # Handle successful API response
            messages.success(request, 'Data submitted successfully')
        else:
            # Handle failed API response
           messages.error(request, 'Failed to submit data')

    return render(request, 'registerIPO.html')


def manageIpo(request):
    # Fetch IPO data from your API
    response = requests.get('http://127.0.0.1:8000/api/ipos/')
    upcoming_ipos = response.json()
    
    # Render the template with IPO data
    return render(request, 'manageipo.html', {'upcoming_ipos': upcoming_ipos})