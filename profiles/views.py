from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from services.models import Appointment


@login_required
def profile(request):
    # Display the user's profile.
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
        else:
            messages.error(request, 'Update Failed. '
                           ' Please Ensure Form Is Valid')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    appointments = profile.appointments.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'appointments': appointments,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    # Display the user's Order History.
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def edit_appointment(request):
    # Display the user's past appointment form for editing.
    return redirect('edit_appointment')


@login_required
def delete_appointment(request, appointment_id):
    # Delete an appointment
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    messages.success(request, 'Appointment deleted!')
    return redirect('profile')
