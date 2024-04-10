#importing from local files 
from session_api.models import Employee
from session_api.serializer import EmployeeSerializer 

# importing classes  form rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination


''' In Both the classes 

   1) authentication_classes and permissions_classes defines which types of authentication and permissions are being used
   2) EmployeeSerialzer is a serializer that serializeremployee data
   3) PageNumberPagination class is used for pagination
   4) request.session.clear_expired() is used to clear the expired session from database

'''
class EmployeeListCreateView(APIView):
        '''
            This classed based view is responsible for get and post method for the employees
            It contains SessionAuthentication and pagination  
        '''

        authentication_classes = [SessionAuthentication]
        permission_classes = [IsAuthenticated]  
        
        
        def get(self , request, format=None):

            request.session.clear_expired() 
           
            # retriving all the data of employee     
            queryset = Employee.objects.all() 
            paginator = PageNumberPagination() # making a object of PageNumberPagination class

            #paginate_queryset is a method which paginate the queryset of employee 
            paginated_queryset = paginator.paginate_queryset(queryset, request)  
           
            # Here EmployeeSerializer  is converting the Employee objects to python dictionary
            serialize = EmployeeSerializer(paginated_queryset, many=True)

            # once the data is converted to the python dictionary then Response method is responsible to convert python dictionary to JSON 
            '''return Response(serialize.data) --> You can return this also but you wont get 
            
                count": 113,
                "next": "http://127.0.0.1:8000/api/?page=2",
                "previous": null,
            
            such type of response '''

            return paginator.get_paginated_response(serialize.data)    
        
        # post method 
        def post(self, request, *agrs, **kwargs) :

            request.session.clear_expired() 
            serialized_data = EmployeeSerializer(data=request.data)

            if serialized_data.is_valid():
                serialized_data.save()
                return Response({'msg' : "Employee data saved successfully"})
            return Response(serialized_data.errors)
        
              
class  EmployeeUpdateDeleteView(APIView) :

        '''
        This class based view is responsible for updating the employee based on employee_id, but the updation can only be performed by admin user.

        This class contains SessionBasedAuthentication 
        '''
        authentication_classes = [SessionAuthentication]
        permission_classes = [IsAdminUser] 
        
        def get(self, request , pk, *args, **kwargs):
             
            ''' returns json data of a particular employee based on employee_id '''

            try:
                employee = Employee.objects.get(employee_id=pk) 
            except Employee.DoesNotExist :
                 return Response({"msg" : "Employee does not exist"})
            
            serialize = EmployeeSerializer(employee)

            return Response(serialize.data)


        def put(self , request , pk, *args, **kwargs):

            '''update the employee data, but required all fields'''
            request.session.clear_expired()
            try :
                employee = Employee.objects.get(employee_id=pk)
            except Employee.DoesNotExist :
                 return Response({'msg' : 'No user found'})

            serialized_data = EmployeeSerializer(employee , data=request.data)
            print(serialized_data)

            if serialized_data.is_valid():
                serialized_data.save()

                return Response({'msg' : f"{employee.employee_id} has been updated successfully."} )
            return Response(serialized_data.errors)
                 
        def patch(self , request , pk, *args, **kwargs):

            '''update employee data but only the fields are required which has to be updated.'''

            request.session.clear_expired() 
            try :
                employee = Employee.objects.get(employee_id=pk)
            except Employee.DoesNotExist :
                 return Response({'msg' : 'No user found'})

            serialized_data = EmployeeSerializer(employee , data=request.data , partial=True)

            if serialized_data.is_valid():
                serialized_data.save()

                return Response({'msg' : f"{employee.employee_id} has been updated successfully."} )
            return Response(serialized_data.errors)
        
        def delete(self , request, pk , *args, **kwargs):

            '''Delete employee data from the database based on the employee id.'''

            request.session.clear_expired() 
            try :
                employee = Employee.objects.get(employee_id=pk)
            except Employee.DoesNotExist :

                return Response({'msg' : 'Employee does not exist'})

            employee.delete()
            return Response({'msg' : 'Employee deleted'})