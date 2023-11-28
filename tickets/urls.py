from rest_framework import routers

from tickets.views import TicketViewSet, OrderViewSet


router = routers.DefaultRouter()
router.register("tickets", TicketViewSet)
router.register("orders", OrderViewSet)


urlpatterns = router.urls


app_name = "tickets"
