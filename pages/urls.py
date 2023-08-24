from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vision-and-mission/', views.vision_and_mission, name='vision_and_mission'),
    path('organizational-chart/', views.organizational_chart, name='organizational_chart'),
    path('board-of-trustees/', views.board_of_trustees, name='board_of_trustees'),
    path('article-of-association/', views.article_of_association, name='article_of_association'),
    path('partners-and-networks/', views.partners_and_networks, name='partners_and_networks'),
    path('states-of-operations/', views.states_of_operations, name='states_of_operations'),
    path('hansen-disease/', views.hansen_disease, name='hansen_disease'),
    path('tuberculosis/', views.tuberculosis, name='tuberculosis'),
    path('ntds/', views.ntds, name='ntds'),
    path('buruli-ulcer/', views.buruli_ulcer, name='buruli_ulcer'),
    path('cbid/', views.cbid, name='cbid'),
    path('aids/', views.aids, name='aids'),
    path('ongoing-projects/', views.ongoing_projects, name='ongoing_projects'),
    path('past-projects/', views.past_projects, name='past_projects'),
    path('publications/', views.publications, name='publications'),
    path('management/', views.management_team, name='management_team'),
    path('child-safeguarding/', views.child_safeguarding, name='child_safeguarding'),
    path('gender-policy/', views.gender_policy, name='gender_policy'),
    path('donate/', views.donation, name='donation'),
    path('contact-us/', views.contact_us, name='contact_us'),
]
