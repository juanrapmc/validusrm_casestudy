from django.contrib import admin

# Register your models here.
from capital_call import models

admin.site.register(models.Funds)
admin.site.register(models.FundCommitment)
admin.site.register(models.FundCall)
admin.site.register(models.FundInvestment)
