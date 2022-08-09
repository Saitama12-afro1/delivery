from django import forms
from .models import Client, Delivery

class CreateClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ("number_client", "mobile_operator_cod", "timezone")
       
    tag = forms.CharField(max_length = 100)

class UpdateForm(forms.ModelForm):#убрать 

    class Meta:
        model = Client
        fields = ("number_client", "mobile_operator_cod", "timezone")
    tag = forms.CharField(max_length=100)
    

class DeliveryForm(forms.ModelForm):
    date_start_sending = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
    date_end_sending = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
    message = forms.CharField(max_length=1000, widget= forms.Textarea)#сделать нормальное поле для ввода текста, широкое
    class Meta:
        model = Delivery
        fields = ( "filter_type", "value_filter")
        