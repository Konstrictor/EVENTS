from django.urls import path, include
from rest_framework import routers
from .views import *
from .api import *

router = routers.DefaultRouter()
router.register("profile", ProfileViewset)
router.register("ticket", TicketViewset)
router.register("payment", PaymentViewset)
router.register("product", ProductViewset)
router.register("consommation", ConsommationViewset)
# router.register("chart_menus", ChartRecetteViewset, basename='chart_menus')

urlpatterns = [
    path("api/", include(router.urls)),
	path("", include(router.urls)),
]