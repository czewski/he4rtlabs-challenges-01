from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import MyForm


def home_view(request):
    context = {}
    return render(request, 'index.html', context)

def result_view(request):
    context = {}

    if request.POST:
        form = MyForm(request.POST)
        if form.is_valid():    
            dailytime = form.cleaned_data['dailytime']
            weekdays = form.cleaned_data['weekdays']
            vacationdays = form.cleaned_data['vacationdays']
            totalprice = form.cleaned_data['totalprice']
            valor_horas = (totalprice / (weekdays * 4 * dailytime) ) + ( ( vacationdays * weekdays * dailytime) )
            context['valor_horas'] = str(valor_horas)
            HttpResponseRedirect('result')

        else:
            form = MyForm()
            HttpResponseRedirect('home')

    return render(request, 'personal/result.html', context)