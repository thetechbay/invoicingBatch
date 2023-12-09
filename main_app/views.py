from django.shortcuts import render
from django.conf import settings
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import Serializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group, User
from rest_framework import status
from django.db.models import Subquery
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
# Create your views here.



@api_view(('POST',))
@permission_classes([AllowAny])
def authenticationData(request):
    if request.method == 'POST':
        email = request.data['email']
        email_verified = request.data['email_verified']
        first_name = request.data['given_name']
        last_name = request.data['family_name']
        picture = request.data['picture']

        if(User.objects.filter(email=email,username=email).exists()):
             # token, created = Token.objects.get_or_create(user=userObj)
            userObj = User.objects.get(username=email)
            token, created = Token.objects.get_or_create(user=userObj)

            userCompanyDetails = users.objects.filter(user = userObj)
            res = {
                'token':token.key,
                'company': userCompanyDetails
            }
            return Response(res)
        else:
            res = {
                'msg':'user does not exist and belongs to any orgainisation, Please contact application supoprt'
            }
            # userObj = User(username=email,password =make_password(first_name+"@1234"), email = email, first_name=first_name, last_name=last_name)
            # userObj.save()
            # obj = userInformation(
            #     email=email,
            #     email_verified = email_verified,
            #     first_name = first_name,
            #     last_name = last_name,
            #     picture = picture,
            #     user=userObj,
            # )
            # print(obj)
            # obj.save();
            # token, created = Token.objects.get_or_create(user=userObj)
            # user= Token.objects.get(key=token.key).user
            
            # res = {
            #     'token':token.key,
            #     'company': companiesClientMappingsSerializer(companyObj,many=True).data,
            # }
            return Response(res)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
def getUnits(request):
    obj = units.objects.all();
    serializer = unitsSerializer(obj,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
def get_tax_units(request):
    obj = taxes.objects.all()
    print(obj)
    serializer = taxesSerializer(obj,many=True)
    print(serializer.data)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(('GET',))
@permission_classes([IsAuthenticated])
def get_client_data(request):
    user  = Token.objects.get(key = request.headers['Authorization'].split(' ')[1]).user
    obj = clients.objects.filter(company = companies.objects.get(customer = customers.objects.get(user=user)))
    serializer = clientsSerializer(obj,many=True)
    return Response(serializer.data)

@api_view(('GET',))
@permission_classes([IsAuthenticated])
def getRecentSales(request):
    user  = Token.objects.get(key = request.headers['Authorization'].split(' ')[1]).user
    obj = sales.objects.filter(company = companies.objects.get(customer = customers.objects.get(user=user))).order_by('-id')
    mainArray = []
    for i in obj:
        print(salesItem.objects.filter(sale = i),"dfg",i)
        serializer = salesSerializer(i)
        print(serializer.data)
        temp_obj = {
            'sales': serializer.data,
            'items': salesItemSerializer(salesItem.objects.filter(sale = sales.objects.get(id=i.id)),many=True).data
        }
        mainArray.append(temp_obj)
    
    # print(serializer.data,"sdf")
    return Response(mainArray)



@api_view(('POST',))
@permission_classes([IsAuthenticated])
def salesData(request):
    if(request.method=='POST'):
        print(request.data);
        invoiceNumber = request.data['invoiceNumber']
        dateOfIssue = request.data['dateOfIssue']
        # billTo = request.data['billTo']
        # billToEmail = request.data['billToEmail']
        # billToAddress = request.data['billToAddress']
        notes = request.data['notes']
        total = request.data['total']
        subTotal = request.data['subTotal']
        amount_in_words = request.data['amountInWords']
        clientBillTo = request.data['clientBillTo']
        currency = request.data['currency']
        items = request.data['items']
        front_random_id = request.data['unique_key']
        if(request.data['taxRate']):
            taxRate = request.data['taxRate']
            taxAmmount = request.data['taxAmmount']
        else:
            taxRate=0.0
            taxAmmount=0.0

        if(request.data['discountRate']):
            discountRate = request.data['discountRate']
            discountAmmount = request.data['discountAmmount']
        else:
            discountRate = 0.0
            discountAmmount=0.0
        clientObj = clients.objects.get(client_unique = clientBillTo)
        if(sales.objects.filter(front_random_id=front_random_id).exists()):
            salesObj = sales.objects.filter(front_random_id=front_random_id)
            salesObj.update(
                company = clientObj.company,
                invoice_id = invoiceNumber,
                invoice_date = dateOfIssue,
                client = clientObj,
                tax_percent = taxRate,
                tax_amount = taxAmmount,
                discount_percent = discountRate,
                discount_amount = discountAmmount,
                subtotal = subTotal,
                currency = currency,
                # due_date = dueDate,
                total_amount = total,
                front_random_id = front_random_id,
                amount_in_words = amount_in_words
            )
            salesObj = salesObj.first()
        else:
            salesObj = sales(
                company = clientObj.company,
                invoice_id = invoiceNumber,
                invoice_date = dateOfIssue,
                client = clientObj,
                tax_percent = taxRate,
                tax_amount = taxAmmount,
                discount_percent = discountRate,
                discount_amount = discountAmmount,
                subtotal = subTotal,
                currency = currency,
                # due_date = dueDate,
                total_amount = total,
                front_random_id = front_random_id,
                amount_in_words = amount_in_words
                # description = description,
            )
            salesObj.save()
        if(salesItem.objects.filter(sale=salesObj).exists()):
            salesItem.objects.filter(sale=salesObj).delete();
        for i in items:
            if(salesItem.objects.filter(sale=salesObj, quantity=i['quantity'],price=i['price'],description=i['description'],name=['name']).exists()):
                print("if me")
                continue;
            else:
                salesItem(
                    sale = salesObj,
                    quantity = i['quantity'],
                    price = i['price'],
                    description = i['description'],
                    name = i['name']
                ).save()
        return Response({'msg':'success'})
    


@csrf_exempt
@api_view(('GET',))
@permission_classes([IsAuthenticated])
def checkInvoiceId(request,id):
    if(sales.objects.filter(invoice_id = id).exists()):
        return Response({'msg':'true'})
    else:
        return Response({'msg':'false'})