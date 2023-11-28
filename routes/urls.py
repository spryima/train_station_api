from rest_framework import routers

from routes.views import RouteViewSet, StationViewSet


router = routers.DefaultRouter()
router.register("routes", RouteViewSet)
router.register("stations", StationViewSet)


urlpatterns = router.urls

app_name = "routes"
