from rest_framework import routers

from journeys.views import JourneyViewSet


router = routers.DefaultRouter()
router.register("journeys", JourneyViewSet)


urlpatterns = router.urls


app_name = "journeys"
