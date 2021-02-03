from rest_framework import serializers
from .models import Brand, Card, Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    cardholder = PersonSerializer()
    brand_name = BrandSerializer()

    class Meta:
        model = Card
        fields = '__all__'