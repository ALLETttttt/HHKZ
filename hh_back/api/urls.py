from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token
# from api.views.apiRequests import MyVacancy
# from api.views.cbv import VacancyListApi, VacancyDetailApi

urlpatterns = [
    path('login/', obtain_jwt_token),

    # Companies
    path('companies/', views.CompanyListApi.as_view()),
    path('companies/<int:company_id>/', views.CompanyDeatailApi.as_view()),
    path('companies/<int:company_id>/vacancies/', views.company_by_vacancy),

    # Vacancies
    path('vacancies/', views.VacancyListApi.as_view()),
    path('vacancies/<int:vacancy_id>/', views.VacancyDetailApi.as_view()),
    path('vacancies/top_ten/', views.top10_vacancies)

]