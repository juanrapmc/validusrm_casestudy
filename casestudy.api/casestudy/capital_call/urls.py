from django.urls import path, include
from rest_framework.routers import DefaultRouter
from capital_call import views


router = DefaultRouter()
router.register(r'funds', views.FundViewSet)
router.register(r'fundcommitments', views.FundCommitmentViewSet)
router.register(r'fundcalls', views.FundCallViewSet)
router.register(r'fundinvestments', views.FundInvestmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
