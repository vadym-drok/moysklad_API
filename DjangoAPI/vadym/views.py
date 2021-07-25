from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Order
from .serializers import OrderSerializer
from django.views.decorators.csrf import csrf_exempt

import requests
import datetime

import environ

env = environ.Env()
environ.Env.read_env()  # reading .env file


def get_data():
    # take information from 'moysklad.ru' for the last 7 days
    headers = {
    'Authorization': 'Basic <Credentials>',
    }

    today = datetime.datetime.today().replace(microsecond=0)
    week_ago = today - datetime.timedelta(days=7)

    params = (
        ('filter', 'updated>'+str(week_ago)),  # time filter for data
    )

    response = requests.get('https://online.moysklad.ru/api/remap/1.2/entity/customerorder', headers=headers,  params=params, auth=(env('MOYSKLAD_LOGIN'), env('MOYSKLAD_PASSWORD')))

    json_data = response.json() # conver json response
    return json_data


@csrf_exempt
def orderApi(request, id=0):

    def post_or_get(orders_data):
        # if the data is in the db: Update it / if not:  write data in db
        try:
            orders = Order.objects.get(id=orders_data['id'])
            orders_serializer= OrderSerializer(orders,data=orders_data)
            if orders_serializer.is_valid():
                orders_serializer.save()
        except:
            orders_serializer= OrderSerializer(data=orders_data)
            if orders_serializer.is_valid():
                orders_serializer.save()

    if request.method=='POST':
        orders_data = JSONParser().parse(request)
        post_or_get(orders_data)
        return JsonResponse("POST Successfully", safe=False)

    elif request.method=='GET':
        json_data = get_data()
        for x in json_data['rows']:
            # take "id" and "sum" from each order 
            orders_data = {
                    "id": x['id'],
                    "sum": x['sum']
                    }
            post_or_get(orders_data)
            
        return JsonResponse("GET Successfully", safe=False)
