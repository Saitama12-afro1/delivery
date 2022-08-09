from django.db import models

#Сущность "клиент" имеет атрибуты:
#уникальный id клиента
#номер телефона клиента в формате 7XXXXXXXXXX (X - цифра от 0 до 9)
# код мобильного оператора
#тег (произвольная метка)(ManyToMany or OneTomany)
#часовой пояс (?????)

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    
    class Meta:
        db_table = "tag"

class Client(models.Model):
    number_client = models.DecimalField(max_digits=11, decimal_places=0)
    mobile_operator_cod = models.PositiveSmallIntegerField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE) 
    timezone = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"{self.number_client} {self.mobile_operator_cod} {self.tag} {self.timezone}"
    
    class Meta:
        db_table = "client"

# Сущность "рассылка" имеет атрибуты
# уникальный id рассылки
# дата и время запуска рассылки
# текст сообщения для доставки клиенту
# фильтр свойств клиентов, на которых должна быть произведена рассылка (код мобильного оператора, тег)(OneTOMany)
# дата и время окончания рассылки


class Delivery(models.Model):#фильтр добавить
    date_start_sending = models.DateTimeField()
    date_end_sending = models.DateTimeField()
    
    mes = models.CharField(max_length = 1000)
    filter_type = models.CharField(max_length=25)
    value_filter = models.CharField(max_length=100)
    class Meta:
        db_table = "delivery"

class Message(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    client = models.ManyToManyField(Client)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    class Meta:
        db_table = "message"

 