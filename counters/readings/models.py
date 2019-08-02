from django.db import models

class Counter(models.Model):
    class Meta:
        verbose_name = "Лічильник"
        verbose_name_plural = "Лічильники"

    identifier = models.CharField(max_length=30, verbose_name="Показання")

    def __str__(self):
        return self.identifier

class Reading(models.Model):
    counter = models.ForeignKey(Counter, on_delete=models.CASCADE)
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(verbose_name="Час зчитування значення лічильника")

    def __str__(self):
        return f"{self.counter}: {self.value} ({self.read_at})"
        