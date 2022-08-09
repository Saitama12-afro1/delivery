from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateClient, UpdateForm, DeliveryForm
from .models import Client, Tag, Delivery


def index(request):
    deliveries = Delivery.objects.all()
    return render(request, "delivery/index.html", {"deliveries":deliveries})

def create_client(request):
    create_client_form = CreateClient()
    if request.method == "POST":
        create_client_form = CreateClient(request.POST)
        
        if create_client_form.is_valid():
            number = create_client_form.cleaned_data["number_client"]
            mobile_operator_cod = create_client_form.cleaned_data["mobile_operator_cod"]
            tag = create_client_form.cleaned_data["tag"]
            timezone = create_client_form.cleaned_data["timezone"]
            tag = Tag.objects.get_or_create(tag = tag)
            tag[0].client_set.create(number_client = number, mobile_operator_cod = mobile_operator_cod, timezone = timezone)
            return HttpResponseRedirect("/check_clients/")

    return render(request, "delivery/create_client.html", {"create_client_form":create_client_form})

def check_clients(request):
    clients = Client.objects.all()
    return render(request, "delivery/check_client.html", {"clients":clients})

def delete_client(request, id):# обернуть в тру кетч
    client = Client.objects.get(id = id)
    client.delete()
    return HttpResponseRedirect("/check_clients/")
    

def update_client(request, id):
    client = Client.objects.get(id = id)
    updateForm = UpdateForm()
    updateForm.fields['number_client'].widget.attrs['value'] = client.number_client 
    updateForm.fields['mobile_operator_cod'].widget.attrs['value'] = client.mobile_operator_cod
    updateForm.fields['timezone'].widget.attrs['value'] = client.timezone 
    updateForm.fields['tag'].widget.attrs['value'] = client.tag.tag 
    if request.method  == "POST":
        updateForm = UpdateForm(request.POST)
        if updateForm.is_valid():
            number = updateForm.cleaned_data["number_client"]
            mobile_operator_cod = updateForm.cleaned_data["mobile_operator_cod"]
            tag_form = updateForm.cleaned_data["tag"]
            timezone = updateForm.cleaned_data["timezone"]
            Client.objects.filter(pk = client.id).update(number_client = number, mobile_operator_cod = mobile_operator_cod, timezone = timezone)
            Tag.objects.filter(pk = client.tag.id).update(tag = tag_form)
        return HttpResponseRedirect("/check_clients/")
    return render(request, "delivery/update_client.html", {"UpdateForm":updateForm})


def create_delivery(request):
    create_delivery_form = DeliveryForm()
    if request.method == "POST":
        create_delivery_form = DeliveryForm(request.POST)
        if create_delivery_form.is_valid():
            filter_type = create_delivery_form.cleaned_data["filter_type"]
            value_filter = create_delivery_form.cleaned_data["value_filter"]
            date_start_sending = create_delivery_form.cleaned_data["date_start_sending"]
            date_end_sending = create_delivery_form.cleaned_data["date_end_sending"]
            message = create_delivery_form.cleaned_data["message"]
            delivery = Delivery(filter_type = filter_type, value_filter = value_filter,
                                date_start_sending = date_start_sending, date_end_sending = date_end_sending,
                                mes = message)
            delivery.save()
        return HttpResponseRedirect("/")    
    return render(request, "delivery/create_delivery.html", {"create_delivery_form":create_delivery_form})


def update_delivery(request, id):
    delivery = Delivery.objects.get(id = id)
    deliveryForm = DeliveryForm()
    print(delivery.mes)
    deliveryForm.fields['message'].widget.attrs['placeholder'] = delivery.mes
    deliveryForm.fields['date_end_sending'].widget.attrs['value'] = delivery.date_end_sending
    deliveryForm.fields['date_start_sending'].widget.attrs['value'] = delivery.date_start_sending 
    deliveryForm.fields['filter_type'].widget.attrs['value'] = delivery.filter_type 
    deliveryForm.fields['value_filter'].widget.attrs['value'] = delivery.value_filter 
    if request.method  == "POST":
        deliveryForm = DeliveryForm(request.POST)
        if deliveryForm.is_valid():
            message = deliveryForm.cleaned_data["message"]
            date_start_sending = deliveryForm.cleaned_data["date_start_sending"]
            date_end_sending = deliveryForm.cleaned_data["date_end_sending"]
            filter_type = deliveryForm.cleaned_data["filter_type"]
            value_filter = deliveryForm.cleaned_data["value_filter"]
            Delivery.objects.filter(pk = delivery.id).update(mes = message, date_start_sending = date_start_sending,
                                                             date_end_sending = date_end_sending, filter_type = filter_type,
                                                             value_filter = value_filter)
        return HttpResponseRedirect("/")
    return render(request, "delivery/update_delivery.html", {"delivery_form":deliveryForm})


def delete_delivery(request, id):# обернуть в тру кетч
    delivery = Delivery.objects.get(id = id)
    delivery.delete()
    return HttpResponseRedirect("/")