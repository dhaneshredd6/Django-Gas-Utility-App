
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'services/home.html')

@login_required
def my_requests(request):
    user_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'services/my_requests.html', {'user_requests': user_requests})


def request_service(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_success')  # You’ll create this view next
    else:
        form = ServiceRequestForm()
    return render(request, 'services/request_form.html', {'form': form})

def request_success(request):
    return render(request, 'services/request_success.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'services/register.html', {'form': form})



@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'services/submit_request.html', {'form': form})
@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            return redirect('my_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'services/submit_request.html', {'form': form})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            messages.success(request, 'Your service request has been submitted successfully!')
            return redirect('submit_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'services/submit_request.html', {'form': form})


@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'services/request_list.html', {'requests': requests})

@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'services/request_list.html', {'requests': requests})
@login_required
def user_dashboard(request):
    user = request.user
    all_requests = ServiceRequest.objects.filter(user=user)
    
    stats = {
        'total': all_requests.count(),
        'pending': all_requests.filter(status='Pending').count(),
        'approved': all_requests.filter(status='Approved').count(),
        'rejected': all_requests.filter(status='Rejected').count(),
    }

    return render(request, 'services/dashboard.html', {
        'user': user,
        'stats': stats,
        'requests': all_requests.order_by('-submitted_at')[:5]  # recent 5
    })

@login_required
def user_dashboard(request):
    status_filter = request.GET.get('status')
    if status_filter:
        requests = ServiceRequest.objects.filter(user=request.user, status=status_filter)
    else:
        requests = ServiceRequest.objects.filter(user=request.user)
    
    return render(request, 'services/dashboard.html', {
        'requests': requests,
        'status_filter': status_filter,
    })

@staff_member_required
def staff_dashboard(request):
    requests = ServiceRequest.objects.all().order_by('-submitted_at')
    return render(request, 'services/staff_dashboard.html', {'requests': requests})

@staff_member_required
def approve_request(request, pk):
    req = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        req.status = 'resolved'
        req.save()
    return redirect('staff_dashboard')

@staff_member_required
def reject_request(request, pk):
    req = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        req.status = 'closed'
        req.save()
    return redirect('staff_dashboard')

@staff_member_required
def bulk_resolve(request):
    if request.method == 'POST':
        ids = request.POST.getlist('selected_requests')
        ServiceRequest.objects.filter(id__in=ids).update(status='resolved')
    return redirect('staff_dashboard')


