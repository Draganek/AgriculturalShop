from rest_framework import routers

from .views import EmployeesViewSet, ClientsViewSet

router = routers.SimpleRouter()
router.register(r'employees', EmployeesViewSet)
router.register(r'clients', ClientsViewSet)
