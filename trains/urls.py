from rest_framework import routers

from trains.views import TrainViewSet, TrainTypeViewSet


router = routers.DefaultRouter()
router.register("genres", TrainViewSet)
router.register("actors", TrainTypeViewSet)


urlpatterns = router.urls


app_name = "trains"
