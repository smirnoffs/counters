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
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    name = models.CharField(max_length=30, verbose_name="Имя")
    patronymic = models.CharField(max_length=30, verbose_name="Отчество")

    def __str__(self):
        return f"{self.surname}" + " " + f"{self.name}"[0].upper() + ". " + f"{self.patronymic}"[0].upper() + ". "

    ########################################################################################################################


class Counter(models.Model):
    class Meta:
        verbose_name = "Счетчики"
        verbose_name_plural = "Счетчики"

    city_choice = "Город"
    village_choice = "Село"
    city_choices = [
        (city_choice, "Город"),
        (village_choice, "Село"),
    ]

    faza1 = "Однофазный"
    faza3 = "Трёхфазный"
    faza_choices = [
        (faza1, "Однофазный"),
        (faza3, "Трёхфазный"),
    ]
    rate1 = "1"
    rate2 = "2"
    rate3 = "3"
    rate_choices = [
        (rate1, "Тариф 1"),
        (rate2, "Тариф 2"),
        (rate3, "Тариф 3"),
    ]
    type1 = "Активная +"
    type2 = "Активная + / Активная -"
    type3 = "Активная + / Реактивная +"
    type4 = "Активная +- / Реактивная +-"
    type_choices = [
        (type1, "Активная +"),
        (type2, "Активная + / Активная -"),
        (type3, "Активная + / Реактивная +"),
        (type4, "Активная +- / Реактивная +-"),
    ]
    subscriber1 = "Население"
    subscriber2 = "Железнодорожный"
    subscriber3 = "Юридический"
    subscriber4 = "Комерческий"
    subscriber_choices = [
        (subscriber1, "Население"),
        (subscriber2, "Железнодорожный"),
        (subscriber3, "Юридический"),
        (subscriber4, "Комерческий"),
    ]
    region1 = "Херсонская область"
    region2 = "Николаевская область"
    region3 = "Запорожская область"
    region_choices = [
        (region1, "Херсонская область"),
        (region2, "Николаевская область"),
        (region3, "Запорожская область"),
    ]
    subsidy1 = "Нету"
    subsidy2 = "Есть"
    subsidy_choices = [
        (subsidy1, "Нету"),
        (subsidy2, "Есть"),
    ]

    counter_id = models.CharField(max_length=50, verbose_name="Номер счетчика")
    subsidy = models.CharField(max_length=30, choices=subsidy_choices, default=subsidy1, verbose_name="Субсидия")
    city_or_village = models.CharField(max_length=10, choices=city_choices, default=city_choice,
                                       verbose_name="Город или село")
    faza = models.CharField(max_length=10, choices=faza_choices, default=faza1, verbose_name="Количество фаз")
    rate = models.CharField(max_length=10, choices=rate_choices, default=rate1, verbose_name="Тариф")
    type = models.CharField(max_length=30, choices=type_choices, default=type1, verbose_name="Тип")
    ratio = models.DecimalField(decimal_places=3, max_digits=10, verbose_name="Коэффициент трансформации")
    subscriber = models.CharField(max_length=30, choices=subscriber_choices, default=subscriber1,
                                  verbose_name="Абонент")
    number = models.IntegerField(verbose_name="Количество знаков")
    date_verification = models.DateField(null=True, blank=True, verbose_name="Дата следующей верификации")
    verification_interval = models.IntegerField(null=True, blank=True, verbose_name="Межпроверочный интервал")
    owner = models.CharField(max_length=50, verbose_name="Владелец")
    region = models.CharField(max_length=30, choices=region_choices, default=region1, verbose_name="Область")
    city = models.CharField(max_length=30, verbose_name="Населенный пункт")
    street = models.CharField(max_length=30, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="Номер дома")
    apartment_number = models.IntegerField(null=True, blank=True, verbose_name="Квартира")

    def __str__(self):
        return f"№{self.counter_id}, {self.region}, Владелец: {self.owner}"


class Value(models.Model):
    class Meta:
        verbose_name = "Показания"
        verbose_name_plural = "Показания"

    counter_id = models.ForeignKey(Counter, on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name="Значение:")


class Readings(Counter):
    class Meta:
        proxy = True
        verbose_name = "Внесение показаний"
        verbose_name_plural = "Внесение показаний"






