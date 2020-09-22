from rest_framework import serializers
from capital_call import models


class FundSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Fund
        fields = '__all__'


class FundCommitmentSerializer(serializers.ModelSerializer):
    fund = FundSerializer()

    class Meta:
        model = models.FundCommitment
        fields = '__all__'


class FundCallSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FundCall
        fields = '__all__'


class FundInvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FundInvestment
        fields = '__all__'
