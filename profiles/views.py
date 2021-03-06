"""
This module will render user account page with
all neccessery user information and forms
"""
from datetime import date, timedelta
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.forms import UserDetailsForm
from home.models import SocialIcon
from checkout.models import Order
from .models import UserProfile


@login_required(login_url='/accounts/login/')
def user_account(request):
    """ A view to return account page """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile detailes updated successfully!')

    details_form = UserDetailsForm(instance=profile)
    orders = profile.orders.all().order_by('-id')[:10]
    social = SocialIcon.objects.all()

    template = 'account/account.html'
    context = {
        'form': details_form,
        'orders': orders,
        'socials': social,
        'no_bag': True,
    }
    return render(request, template, context)


@login_required(login_url='/accounts/login/')
def booking_review(request, order_number):
    """ A view to return booking infomration """
    order = get_object_or_404(Order, order_number=order_number)
    lessons_count = order.lineitems.count()

    # Footer social media Icons
    social = SocialIcon.objects.all()

    template = 'account/bookings-review.html'
    context = {
        'order': order,
        'lessons_count':lessons_count,
        'socials': social,
    }

    return render(request, template, context)


@login_required(login_url='/accounts/login/')
def bookings_active(request):
    """ A view to return user active bookings """

    profile = get_object_or_404(UserProfile, user=request.user)

    # Order user orders - newest at begining
    user_orders = profile.orders.all()

    # Filter Booking orders between today and past 60 days - including today's bookings
    start_date = date.today() + timedelta(days=1)
    end_date = start_date + timedelta(days=-59)
    # Filter date range
    user_orders = user_orders.filter(date__range=[end_date, start_date])

    # Sort orders by date - newset first
    user_orders = user_orders.order_by('-date')

    from_booking_active = True
    request.session['from_booking_active'] = from_booking_active

    # Send number of active bookings to session
    request.session['active_booking_count'] = user_orders.count()

    social = SocialIcon.objects.all()
    template = 'account/bookings-active.html'
    context = {
        'user_orders': user_orders,
        'socials': social,
        'from_booking_active': from_booking_active,
    }

    return render(request, template, context)


@login_required(login_url='/accounts/login/')
def bookings_archived(request):
    """ A view to return user archived bookings """

    profile = get_object_or_404(UserProfile, user=request.user)

    # Order user orders - newest at begining
    user_orders = profile.orders.all()

    # Filter Booking older than 60 days
    start_date = date.today() + timedelta(days=-59)
    end_date = start_date + timedelta(days=-365)
    # Filter date range
    user_orders = user_orders.filter(date__range=[end_date, start_date])

    # Sort orders by date - newset first
    user_orders = user_orders.order_by('-date')

    from_booking_archived = True
    request.session['from_booking_archived'] = from_booking_archived

    # Get active booking count
    active_booking_count = request.session.get('active_booking_count')

    social = SocialIcon.objects.all()
    template = 'account/bookings-archived.html'
    context = {
        'user_orders': user_orders,
        'socials': social,
        'from_booking_archived': from_booking_archived,
        'active_booking_count': active_booking_count,
    }

    return render(request, template, context)
