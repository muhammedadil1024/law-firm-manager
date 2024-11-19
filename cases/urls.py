from django.urls import path
from . import views

app_name = "cases"

urlpatterns = [
    # Home url
    path("", views.HomeView.as_view(), name="home"),

    # Client url
    path("clients/", views.ClientListView.as_view(), name="clientlist"),
    path("clients/create/", views.ClientCreateView.as_view(), name="clientcreate"),
    path("clients/<int:pk>/update/", views.ClientUpdateView.as_view(), name="clientupdate"),
    path("clients/<int:pk>/delete/", views.ClientDeleteView.as_view(), name="clientdelete"),

    # Lawyers url
    path("lawyers/", views.LawyerListView.as_view(), name="lawyerlist"),
    path("lawyers/create/", views.LawyerCreateView.as_view(), name="lawyercreate"),
    path("lawyers/<int:pk>/update/", views.LawyerUpdateView.as_view(), name="lawyerupdate"),
    path("lawyers/<int:pk>/delete/", views.LawyerDeleteView.as_view(), name="lawyerdelete"),

    # Cases url
    path("cases/", views.CaseListView.as_view(), name="caselist"),
    path("cases/create/", views.CaseCreateView.as_view(), name="casecreate"),
    path("cases/<int:pk>/update/", views.CaseUpdateView.as_view(), name="caseupdate"),
    path("cases/<int:pk>/delete/", views.CaseDeleteView.as_view(), name="casedelete"),
]
