from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Partner, Network, Donation, Affiliate, Photo
from blog.models import Post
from .forms import ContactForm
import requests

def index(request):
    # posts = Post.published.all()[0:2]
    posts = requests.get("https://weblog.redaid-nigeria.org/wp-json/wp/v2/posts").json()[0:2]

    post_imgs = []

    # for post in posts:
    #     get_post = requests.get(f"https://weblog.redaid-nigeria.org/wp-json/wp/v2/media?parent={post['id']}").json()[0:1]
    #     post_imgs.append(get_post[0]['guid']['rendered'])

    # print(post_imgs)

    # post_img = requests.get(f"https://weblog.redaid-nigeria.org/wp-json/wp/v2/media?parent={posts[0]['id']}").json()[0:1]
    # post = post_img['guid']
    # print(post_img[0]['guid']['rendered'])
    # print(post['guid']['rendered'])
    # posts_img = [img for img in ]
    return render(request, "pages/index.html", {"posts": posts, 'post_imgs': post_imgs})

def gallery(request):
    photos = Photo.objects.all()
    context = {
        'photos': photos
    }
    return render(request, "pages/gallery.html", context)

def vision_and_mission(request):
    return render(request, "pages/vision-and-mission.html")

def organizational_chart(request):
    return render(request, "pages/organizational-chart.html")

def board_of_trustees(request):
    return render(request, "pages/board-of-trustees.html")

def article_of_association(request):
    return render(request, "pages/article-of-association.html")

def partners_and_networks(request):
    partners = Partner.objects.all()
    networks = Network.objects.all()
    affiliates = Affiliate.objects.all()
    context = {
        'partners': partners,
        "networks": networks,
        'affiliates': affiliates,
    }
    return render(request, "pages/partners-and-networks.html", context)

def states_of_operations(request):
    return render(request, "pages/states-of-operations.html")

def hansen_disease(request):
    return render(request, "pages/hansen-disease.html")

def tuberculosis(request):
    return render(request, "pages/tuberculosis.html")

def ntds(request):
    return render(request, "pages/ntds.html")

def buruli_ulcer(request):
    return render(request, "pages/buruli-ulcer.html")

def cbid(request):
    return render(request, "pages/cbid.html")

def aids(request):
    return render(request, "pages/aids.html")

def ongoing_projects(request):
    return render(request, "pages/ongoing-projects.html")

def past_projects(request):
    return render(request, "pages/past-projects.html")

def publications(request):
    return render(request, "pages/publications.html")

def management_team(request):
    return render(request, "pages/management-team.html")

def child_safeguarding(request):
    return render(request, "pages/child-safeguarding.html")

def gender_policy(request):
    return render(request, "pages/gender-policy.html")

def donation(request):
    if request.method == "POST":
        print(request.POST)
        sender = request.POST.get('sender')
        email = request.POST.get('email')
        ref = request.POST.get('ref')
        amount = int(request.POST.get('amount'))
        cause = request.POST.get('cause')
        status = request.POST.get('status')
        message = request.POST.get('message')
        frequency = request.POST.get('frequency')
        tx_ref = request.POST.get('tx_ref')

        Donation.objects.create(
            sender = sender,
            email = email,
            ref = ref,
            amount = amount,
            cause = cause.title(),
            status = status.title(),
            message = message,
            frequency = frequency.title(),
            tx_ref = tx_ref
        )

        messages.success(request, "Payment successful! Thank you for your support.")
        return redirect('vision_and_mission')

    return render(request, "pages/donation.html")

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_form = form.save(commit=False)
            contact_form.save()
            messages.success(request, "Thank you for your message. We will get back to you as soon as we can.")
            return redirect('contact_us')
    else:
        form = ContactForm()

    context = {
        "form": form
    }

    return render(request, "pages/contact.html", context)