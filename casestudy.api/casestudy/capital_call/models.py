from django.db import models


class Funds(models.Model):
    name = models.CharField(max_length=255, unique=True)


class FundCommitment(models.Model):
    fund_id = models.ForeignKey(Funds, on_delete=models.CASCADE, related_name='fund_commitments')
    date = models.DateField()
    amount = models.DecimalField(max_digits=999, decimal_places=2)
    drawn_amount = models.DecimalField(max_digits=999, decimal_places=2, default=0)


class FundCall(models.Model):
    date = models.DateField()
    investment_name = models.CharField(max_length=255)
    capital_requirement = models.DecimalField(max_digits=999, decimal_places=2)


class FundInvestment(models.Model):
    call_id = models.ForeignKey(FundCall, on_delete=models.CASCADE, related_name='call_investments')
    fund_id = models.ForeignKey(Funds, on_delete=models.CASCADE, related_name='fund_investments')
    commitment_id = models.IntegerField()
    investment_amount = models.DecimalField(max_digits=999, decimal_places=2)
