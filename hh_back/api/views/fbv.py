import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


from api.models import Company
from api.serializers import CompanySerializer


@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == 'GET':
        company = Company.objects.all()
        serializer_company = CompanySerializer(company, many=True)
        # company_json = [p.to_json() for p in company]
        return Response(serializer_company.data)
    if request.method == 'POST':
        # data = json.loads(request.body)
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        # company = Company.objects.create(
        #     name = data.get('name', ''),
        #     description = data.get('description', ''),
        #     city = data.get('city', ''),
        #     address = data.get('address', '')
        # )
        # return Response(company.to_json())
    
@api_view(['GET', 'PUT', 'DELETE'])   
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)

    except Company.DoesNotExist as e:
        return Response({'Error': str(e)})
    
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    

    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        # company.name = data.get('name', company.name)
        # company.city = data.get('city', '')
        # company.save()
        # return Response(company.to_json())
    

    if request.method == 'DELETE':
        company.delete()
        return Response({"deleted": True})
    