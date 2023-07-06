from django.shortcuts import render
import json
from django.http.response import JsonResponse
from django.views import View
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt

from api.serializers import CompanySerializer, VacancyModelSerializer

# Create your views here.
@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        company = Company.objects.all()
        serializer_company = CompanySerializer(company, many=True)
        # company_json = [p.to_json() for p in company]
        return JsonResponse(serializer_company.data, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
        # company = Company.objects.create(
        #     name = data.get('name', ''),
        #     description = data.get('description', ''),
        #     city = data.get('city', ''),
        #     address = data.get('address', '')
        # )
        # return JsonResponse(company.to_json())
    
@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)

    except Company.DoesNotExist as e:
        return JsonResponse({'Error': str(e)})
    
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)
    

    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
        # company.name = data.get('name', company.name)
        # company.city = data.get('city', '')
        # company.save()
        # return JsonResponse(company.to_json())
    

    if request.method == 'DELETE':
        company.delete()
        return JsonResponse({"deleted": True})
    
def company_by_vacancy(request, company_id):
    vacancy = Vacancy.objects.filter(company_id=company_id)
    vacancy_json = [p.to_json() for p in vacancy]
    return JsonResponse(vacancy_json, safe=False)


class MyVacancy(View):
    def get(self, request):
        vacancy = Vacancy.objects.all()
        serializer_vacancy = VacancyModelSerializer(vacancy, many=True)
        # vacancy_json = [p.to_json() for p in vacancy]
        return JsonResponse(serializer_vacancy.data, safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        vacancy = Vacancy.objects.create(
            name = data.get('name', ''),
            description = data.get('description', ''),
            salary = data.get('salary', ''),
            company = data.get('company', '')
        )
        serializer = VacancyModelSerializer(vacancy, many=True)
        return JsonResponse(serializer.data, safe=False)



def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)

    except Vacancy.DoesNotExist as e:
        return JsonResponse({'Error': str(e)})
    
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    

    if request.method == 'PUT':
        data = json.loads(request.body)
        vacancy.name = data.get('name', vacancy.name)
        vacancy.salary = data.get('salary', '')
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    

    if request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({"deleted": True})

def top10_vacancies(request):
    top10_vacancies = Vacancy.objects.all().order_by('-salary')
    top10_vacancies = top10_vacancies[:10]
    top10_vacancies_json = [p.to_json() for p in top10_vacancies]
    return JsonResponse(top10_vacancies_json, safe=False)