from django.shortcuts import render

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
    return render(request, "pages/partners-and-networks.html")

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

# def buruli_ulcer(request):
#     return render(request, "pages/buruli-ulcer.html")