from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'statuses', StatusViewSet)

urlpatterns = router.urls
