from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Job, Profile, Purchase, Review
from .forms import JobForm

# Create your views here.
def home(request):
    jobs = Job.objects.filter(status=True)
    return render(request, 'home.html', {"jobs": jobs})

def job_detail(request, id):
    if request.method == 'POST' and \
        not request.user.is_anonymous() and \
        Purchase.objects.filter(job_id=id, buyer=request.user).count() > 0 and \
        'content' in request.POST and \
        request.POST['content'].strip() != '':
        Review.objects.create(content=request.POST['content'], job_id=id, user=request.user)
    
    try:
        job = Job.objects.get(id=id)
    except Job.DoesNotExist:
        return redirect('/')
    
    if request.user.is_anonymous() or \
    Purchase.objects.filter(job=job, buyer=request.user).count() == 0 or \
    Review.objects.filter(job=job, user=request.user).count() > 0:
        show_post_review = False
    else:
        show_post_review = Purchase.objects.filter(job=job, buyer=request.user).count() > 0
    review = Review.objects.filter(job=job)
    return render(request, 'job_detail.html', {"show_post_review": show_post_review, "reviews": review, "job": job})

@login_required(login_url="/")
def create_job(request):
    error = ''
    if request.method == 'POST':
        job_form = JobForm(request.POST, request.FILES)
        if job_form.is_valid():
            job = job_form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('my_jobs')
        else:
            error = "Data is not valid"

    job_form = JobForm()
    return render(request, 'create_job.html', {"error": error})

@login_required(login_url="/")
def edit_job(request, id):
    try:
        job = Job.objects.get(id=id, user=request.user)
        error = ''
        if request.method == 'POST':
            job_form = JobForm(request.POST, request.FILES, instance=job)
            if job_form.is_valid():
                job.save()
                return redirect('my_jobs')
            else:
                error = "Data is not valid"

        return render(request, 'edit_job.html', {"job": job, "error": error})
    except Job.DoesNotExist:
        return redirect('/')

@login_required(login_url="/")
def my_jobs(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'my_jobs.html', {"jobs": jobs})

def profile(request, username):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.about = request.POST['about']
        profile.slogan = request.POST['slogan']
        profile.save()
    else:
        try:
            profile = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            return redirect('/')
    
    jobs = Job.objects.filter(user=profile.user, status=True)
    return render(request, 'profile.html', {"profile": profile, "jobs": jobs})

@login_required(login_url="/")
def create_purchase(request):
    if request.method == 'POST':
        try:
            job = Job.objects.get(id = request.POST['job_id'])
        except Job.DoesNotExist:
            return redirect('/')

        nonce = request.POST["payment_method_nonce"]
        
        if result.is_success:
            Purchase.objects.create(job=job, buyer=request.user)

    return redirect('/')

@login_required(login_url="/")
def penjualan(request):
    purchases = Purchase.objects.filter(job__user=request.user)
    return render(request, 'penjualan.html', {"purchases": purchases})

@login_required(login_url="/")
def pembelian(request):
    purchases = Purchase.objects.filter(buyer=request.user)
    return render(request, 'Pembelian.html', {"purchases": purchases})

def category(request, link):
    categories = {
        "graphics-design": "GD",
        "digital-marketing": "DM",
        "video-animation": "VA",
        "music-audio": "MA",
        "programming-tech": "PT"
    }
    try:
        jobs = Job.objects.filter(category=categories[link])
        return render(request, 'home.html', {"jobs": jobs})
    except KeyError:
        return redirect('home')

def search(request):
    jobs = Job.objects.filter(title__contains=request.GET['title'])
    return render(request, 'home.html', {"jobs": jobs})