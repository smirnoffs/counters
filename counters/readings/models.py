from django.db import models


class Address(models.Model):
    class Meta:
        verbose_name = "Адреса"
        verbose_name_plural = "Адреса"

    city = models.CharField(max_length=30, verbose_name="Город, населенный пункт")
    street = models.CharField(max_length=30, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="Номер дома", null=True, blank=True)
    hull_number = models.CharField(null=True, blank=True, max_length=5, verbose_name="Корпус")
    apartment_number = models.IntegerField(null=True, blank=True, verbose_name="Квартира")

    def __str__(self):

        if (f"{self.hull_number}" != "None" and f"{self.apartment_number}" != "None"):
            return f"{self.city} {self.street} {self.house_number}" + " Квартира " + f"{self.apartment_number}" + " Корпус " + f"{self.hull_number}"
        elif (f"{self.apartment_number}" != "None"):
            return f"{self.city} {self.street} {self.house_number}" + " Квартира " + f"{self.apartment_number}"
        elif (f"{self.hull_number}" != "None"):
            return f"{self.city} {self.street} {self.house_number}" + " Корпус " + f"{self.hull_number}"
        else:
            return f"{self.city} {self.street} {self.house_number}"


class Owners(models.Model):
    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владелец"
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)
    surname = models.CharField(max_length=30, verbose_name = "Фамилия")
    name = models.CharField(max_length=30, verbose_name = "Имя")
    patronymic = models.CharField(max_length=30, verbose_name = "Отчество")
    
    def __str__(self):
        return f"{self.surname}" + " " + f"{self.name}"[0].upper() + ". "  + f"{self.patronymic}"[0].upper()+ ". " 


class Counter(models.Model):
    class Meta:
        verbose_name = "Лічильник"
        verbose_name_plural = "Лічильники"

    owner = models.ForeignKey(Owners, null=True, blank=True, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=30, verbose_name="Id")

    def __str__(self):
        return f"{self.identifier} ({self.owner, self.address})"


class Value(models.Model):
    class Meta:
        verbose_name = "Показания"
        verbose_name_plural = "Показания"
    
    counter = models.ForeignKey(Counter, on_delete = models.CASCADE)
    value = models.IntegerField(verbose_name="Значение:")




