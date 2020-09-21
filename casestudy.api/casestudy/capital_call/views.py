from rest_framework import viewsets
from capital_call.models import Fund, FundCall, FundCommitment, FundInvestment
from capital_call.serializers import (
    FundSerializer,
    FundCallSerializer,
    FundCommitmentSerializer,
    FundInvestmentSerializer
)

class FundViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer


class FundCommitmentViewSet(viewsets.ModelViewSet):
    queryset = FundCommitment.objects.all()
    serializer_class = FundCommitmentSerializer


class FundCallViewSet(viewsets.ModelViewSet):
    queryset = FundCall.objects.all()
    serializer_class = FundCallSerializer


class FundInvestmentViewSet(viewsets.ModelViewSet):
    queryset = FundInvestment.objects.all()
    serializer_class = FundInvestmentSerializer
