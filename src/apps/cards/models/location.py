from django.contrib.gis.db import models  # изменён импорт

class Place(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название места")
    location = models.PointField(verbose_name="Локация")  # ← добавляем PointField

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"