from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
import logging

logger = logging.getLogger(__name__)

def index(request):
     return HttpResponse(submit_request(request))

def submit_request(request):
    # return HttpResponse(submit_request)
    try:
        if request.method == 'POST':
            form = ServiceRequestForm(request.POST, request.FILES)
            if form.is_valid():
            # Create a new service request object
                service_request = form.save(commit=False)
                service_request.customer = request.user  # Assign the current user as the customer
                service_request.save()
                return redirect('track_request', request_id=service_request.id)  # Redirect to request tracking page
        else:
            form = ServiceRequestForm()
        return HttpResponse(request, 'submit_request.html', {'form': form})
    except Exception as e:
        logger.error('Error submitting service request: %s', e)

def track_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'track_request.html', {'service_request': service_request})

@login_required
def view_account(request):
    customer = request.user
    return render(request, 'view_account.html', {'customer': customer})
    