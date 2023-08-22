from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Partner, Network
from .forms import ContactForm

def index(request):
    return render(request, "pages/index.html")

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
    context = {
        'partners': partners,
        "networks": networks
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

def donation(request):
    if request.method == "POST":
        # print(request.POST)
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