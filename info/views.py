from django.shortcuts import render
from .models import Person, Contact

def home(request):
    return render(request, 'info/home.html')

def about(request):
    return render(request, 'info/about.html')

def contact(request):
    contact = Contact.objects.first()  # Gets the first contact record
    return render(request, 'info/contact.html', {'contact': contact})

def team(request):
    team_members = Person.objects.all()
    return render(request, 'info/team.html', {'team': team_members})

def why(request):
    return render(request, 'info/why.html')

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages  # Import Django's messages framework

def price_inquiry(request):
    if request.method == 'POST':
        # Collect form data
        fullname = request.POST.get('fullname')
        company = request.POST.get('company')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact_method = request.POST.get('contactMethod')

        type_of_goods = request.POST.get('type_of_goods')
        goods_description = request.POST.get('goods_description')
        total_weight = request.POST.get('total_weight')
        dimensions = request.POST.get('dimensions')
        num_packages = request.POST.get('num_packages')
        cargo_value = request.POST.get('cargo_value')
        special_handling = request.POST.get('special_handling')

        pickup_location = request.POST.get('pickup_location')
        delivery_location = request.POST.get('delivery_location')
        shipping_method = request.POST.get('shipping_method')
        shipping_date = request.POST.get('shipping_date')
        delivery_deadline = request.POST.get('delivery_deadline')

        # Optional server-side validation for required fields:
        if not (fullname and company and email and phone and contact_method):
            return HttpResponse("Error: Please fill out all required contact fields.", status=400)

        # Build the email message
        message_body = f"""
        New Price Inquiry Submission:

        --- Contact Information ---
        Full Name: {fullname}
        Company: {company}
        Email: {email}
        Phone: {phone}
        Preferred Contact Method: {contact_method}

        --- Shipment Details ---
        Type of Goods: {type_of_goods}
        Description of Goods: {goods_description}
        Total Weight (kg): {total_weight}
        Dimensions: {dimensions}
        Number of Packages: {num_packages}
        Cargo Value: {cargo_value}
        Special Handling Requirements: {special_handling}

        --- Transportation Details ---
        Pickup Location: {pickup_location}
        Delivery Location: {delivery_location}
        Preferred Shipping Method: {shipping_method}
        Expected Shipping Date: {shipping_date}
        Delivery Deadline: {delivery_deadline}
        """

        # Send the email
        send_mail(
            subject="New Price Inquiry",
            message=message_body,
            from_email=settings.DEFAULT_FROM_EMAIL,  # Make sure this is configured
            recipient_list=["social.emertatfarabar@gmail.com"],
        )

        # Use Django messages to show success once
        messages.success(request, "Your request has been sent successfully!")

        # Redirect using the named URL pattern or direct path
        return redirect('/price-inquiry')  
        # or: return redirect('/price-inquiry')

    # If GET, show the form
    return render(request, 'info/price_inquiry.html')