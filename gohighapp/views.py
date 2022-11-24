from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import *
from rest_framework.decorators import action
from .forms import *


class ContactViewSet(APIView):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def get(self, request):
        authe_resp=contact()
        # custField=authe_resp.customField
        # print(custField,"custField")
        context={
            "data":authe_resp,
            # "cust_field": custField
        }    
        return render(request, "get_contact.html",context=context)

def ContactEditViewSet(request, pk):
    context ={}
    data_id=pk
    authe_resp=cust_field(data_id)
    context={
        "data": authe_resp,
    }
    if request.method == 'POST':
        data=request.POST
        pk=request.POST.get("key_id")
        name=request.POST.get("name")
        res=cust_field_put(pk,name)
        return redirect('home')
    return render(request, 'edit_contact.html', context)     