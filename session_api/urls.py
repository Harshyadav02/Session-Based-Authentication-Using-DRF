from django.urls import path, include
from session_api.views import EmployeeListCreateView,EmployeeUpdateDeleteView

'''url for the CRUD operations of employee'''
urlpatterns = [
    path('api/', EmployeeListCreateView.as_view(), name='api'),
    path('api/<int:pk>/', EmployeeUpdateDeleteView.as_view(), name='employee-update'),
]
 
