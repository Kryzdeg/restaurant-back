from rest_framework import routers
from .api import MealModelViewSet

router = routers.SimpleRouter()
router.register(r'meals', MealModelViewSet)
urlpatterns = router.urls