import joblib
import numpy as np
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import approvals
from .serializers import ApprovalsSerializer


class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = ApprovalsSerializer


@api_view(["POST"])
def approvereject(request):
    try:
        mdl = joblib.load("/Users/egortitenkov/PycharmProjects/scratch_diplom/DjangoAPI/MyAPI/loan_model.pkl")
        mydata = request.data
        unit = np.array(list(mydata.values()))
        unit = unit.reshape(1, -1)
        scalers = joblib.load("/Users/egortitenkov/PycharmProjects/scratch_diplom/DjangoAPI/MyAPI/scalers.pkl")
        X = scalers.transform(unit)
        y_pred = mdl.predict(X)
        y_pred = (y_pred > 0.58)
        newdf = pd.DataFrame(y_pred, columns=['Status'])
        newdf = newdf.replace({True: 'Approved', False: 'Rejected'})
        return JsonResponse('Your Status is {}'.format(newdf), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def form_handler(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        dependants = int(request.POST.get('dependants'))
        applicantincome = int(request.POST.get('applicantincome'))
        coapplicantincome = request.POST.get('coapplicantincome')
        loanamt = int(request.POST.get('loanamt'))
        loanterm = int(request.POST.get('loanterm'))
        credithstory = request.POST.get('credithstory')
        gender = request.POST.get('gender')
        married = request.POST.get('married')
        graduated = request.POST.get('graduated')
        self_employed = request.POST.get('self_employed')
        property = request.POST.get('property')

        if gender == 'Male' and applicantincome > loanamt and (property == 'Belarus') or (
                property == 'Russia') and (
                loanterm <= 360) and (
                loanamt < 1000000) and self_employed == 'Yes' and married == 'No' and graduated == 'Graduated':
            result = 'Approved'
        elif (loanamt > 1000000) and (property == 'USA') or (property == 'Russia') and (loanterm <= 360) and (
                loanamt <= 1000000) and (dependants == True) and (
                married == 'Yes') or graduated == 'Graduated':
            result = 'Rejected'
        else:
            result = 'Rejected'

        return render(request, 'result.html', {'result': result})
    else:
        return render(request, 'form.html')
