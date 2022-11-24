import csv
import io
import os
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from loader.models import Client, Org, Service, Bill
from loader.serializers import LoadSerializer, BillSerializer


def check_date(date: str) -> bool:
    correct_date = None
    try:
        datetime.strptime(date or "", "%d.%m.%Y")
        correct_date = True
    except ValueError:
        correct_date = False
    return correct_date


class LoadDataAPIView(GenericAPIView):
    serializer_class = LoadSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            file = serializer.validated_data['file'].read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(file))
            # Bill.objects.all().delete()
            for line in reader:
                client, created = Client.objects.get_or_create(name=line['client_name'])
                org, created = Org.objects.get_or_create(name=line['client_org'])
                service = None
                if line['service'] != '' and line['service'] != '-':
                    service, created = Service.objects.get_or_create(name=line['service'])
                if line['sum'].isdigit() and line['№'].isdigit() and check_date(line['date']):
                    try:
                        Bill.objects.get(clorgid=line['№'], client=client, org=org)
                        return Response('dublicate № bill', status=status.HTTP_400_BAD_REQUEST)
                    except ObjectDoesNotExist:
                        date = datetime.strptime(line['date'], "%d.%m.%Y").strftime('%Y-%m-%d')
                        Bill.objects.create(client=client, org=org, service=service, sum=line['sum'], date=date,
                                            clorgid=line['№'])
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response('invalid fail', status=status.HTTP_400_BAD_REQUEST)


class GetBillsAPIVIew(ListAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()
