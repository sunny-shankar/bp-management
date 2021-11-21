from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import UserAccount, BloodPressure
from datetime import datetime


def index(request):
    users = UserAccount.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        systolic = request.POST['systolic']
        diastolic = request.POST['diastolic']
        user = UserAccount.objects.get(username=username)
        data = BloodPressure(
            user=user, systolic=systolic, diastolic=diastolic)
        data.save()
        return redirect('view')
    return render(request, 'management/index.html', {'users': users})


def view(request):
    users = UserAccount.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        return redirect('user-view', pk=username)
    return render(request, 'management/view.html', {'users': users})


def user_view(request, pk):
    user = UserAccount.objects.get(username=pk)
    data = BloodPressure.objects.filter(user=user)
    if request.method == 'POST':
        return redirect('chart', pk=user.username)
    return render(request, 'management/user-view.html', {'user': user, 'data': data})


def create_user(request):
    if request.method == 'POST':
        try:
            user = UserAccount(
                username=request.POST['username'], mail=request.POST['mail'], age=request.POST['age'])
            user.save()
        except:
            return HttpResponse('Username Must be Unique')
        return redirect('index')
    return render(request, 'management/create.html', {})


def chart(request, pk):
    user = UserAccount.objects.get(username=pk)
    data = BloodPressure.objects.filter(user=user)
    context = {}
    context['Systolic'] = []
    context['Diastolic'] = []
    context['DateTime'] = []
    context['User'] = {
        'username': user.username,
        'age': user.age,
    }

    for each_data in data:
        context['Systolic'].append(each_data.systolic)
        context['Diastolic'].append(each_data.diastolic)
        context['DateTime'].append(
            each_data.datetime.strftime("%m/%d/%Y, %H:%M:%S"))
    print(context['DateTime'])

    return render(request, 'management/chart.html', context)
