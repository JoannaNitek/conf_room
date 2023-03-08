from django.urls import path, include
from rest_framework import routers
from .views import RoomViewSet, ReservationViewSet

router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)

# urlpatterns = [
#     path(r'', include(router.urls))
# ]
urlpatterns = router.urls