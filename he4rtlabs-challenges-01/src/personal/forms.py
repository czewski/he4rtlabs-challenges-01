from django import forms

class MyForm(forms.Form):
    class Meta:
        fields = ('dailytime', 'weekdays', 'vacationdays', 'totalprice')
    dailytime = forms.FloatField(label='dailytime', max_value=24, min_value=0)
    weekdays = forms.FloatField(label='weekdays', max_value=7, min_value=0)
    vacationdays = forms.FloatField(label='vacationdays', max_value=60, min_value=0)
    totalprice = forms.FloatField(label='totalprice', max_value=50000, min_value=0)
    


