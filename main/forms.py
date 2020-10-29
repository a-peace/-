from . models import Contract, Timing
from django.forms import ModelForm


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'


class TimingForm(ModelForm):
    class Meta:
        model = Timing
        fields = '__all__'
