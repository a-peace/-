import decimal

from django.shortcuts import render, redirect
from .models import Contract, Timing
from .forms import ContractForm, TimingForm
import datetime


def index(request):
    contracts = Contract.objects.all()

    return render(request, 'main/index.html', {'title': 'Название вкладки: главная страница', 'contracts': contracts})


def create(request):
    form = ContractForm()
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            contract = Contract.objects.last()
            return redirect('create_timing', contract.id)
    context = {'form': form}
    return render(request, 'main/create.html', context)


def about(request):
    return render(request, 'main/about.html')


def schedule(request):
    return render(request, 'main/schedule.html')


def table(request, contract_id):

    days = 0
    contract = Contract.objects.get(id=contract_id)
    timing = contract.timing_set.all()

    # Получение и обновление даты today
    n = datetime.datetime.date(datetime.datetime.now())

    # Начисление неустойуки
    for i in timing:
        if i.contract.side == 'Покупатель' and i.reaction == 'Не выполнено' and n > i.execution_period:
            days = (n - i.execution_period).days
            if days > i.days:
                i.penalty += round(decimal.Decimal(0.001 * abs(-i.days + days)) *
                                   (i.subject - i.delivered) * i.amount / i.subject, 2)
                i.days = days
                i.save()
        elif i.contract.side == 'Поставщик' and i.reaction == 'Не выполнено' and n > i.payment_period:
            days = (n - i.payment_period).days
            if days > i.days:
                i.penalty += round(decimal.Decimal(0.001 * abs(-i.days + days))
                                   * (i.amount - i.paid), 2)
                i.days = days
                i.save()

                context = {'title': 'Сроки договора', 'contract': contract, 'timing': timing, 'n': n, 'days': days}

    return render(request, 'main/table.html', context)


def uploads(request):
    return render(request, 'main/uploads.html')


def update_contract(request, pk):
    contract = Contract.objects.get(id=pk)
    form = ContractForm(instance=contract)

    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'contract': contract}
    return render(request, 'main/create.html', context)


def delete_contract(request, pk):
    contract = Contract.objects.get(id=pk)
    if request.method == "POST":
        contract.delete()
        return redirect('/')

    context = {'item': contract}
    return render(request, 'main/delete_contract.html', context)


def create_timing(request, kek):
    contract = Contract.objects.get(id=kek)
    form = TimingForm(initial={'contract': contract})
    if request.method == 'POST':
        form = TimingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'main/create_timing.html', context)


def update_timing(request, kek):
    timing = Timing.objects.get(id=kek)
    form = TimingForm(instance=timing)

    if request.method == 'POST':
        form = TimingForm(request.POST, instance=timing)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/create_timing.html', context)


def delete_timing(request, kek):
    timing = Timing.objects.get(id=kek)
    if request.method == "POST":
        timing.delete()
        return redirect('/')

    context = {'item': timing}
    return render(request, 'main/delete_timing.html', context)
