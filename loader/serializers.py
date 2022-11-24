from rest_framework import serializers

from loader.models import Bill, Client, Org, Service


class LoadSerializer(serializers.Serializer):
    file = serializers.FileField(required=True)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')


class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = ('__all__')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('__all__')


class BillSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False)
    org = OrgSerializer(many=False)
    service = ServiceSerializer(many=False)

    class Meta:
        model = Bill
        fields = ('client', 'org', 'service', 'clorgid', 'sum', 'date')
