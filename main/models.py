from django.db import models

# arMA7272AR

class Member(models.Model):

    job = models.CharField(max_length=255, verbose_name="Должность 255зн.")
    name = models.CharField(max_length=255, verbose_name="Имя и Фамилия 255зн.")
    img = models.ImageField(upload_to='members/',default='placeholders/placeholder.jpg',blank=True,null=True, verbose_name="Фотография (исключительно квадратные)")
    
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "члена команды"
        verbose_name_plural = "Члены команды"
        ordering = ['name']

class Slide(models.Model):

    desktop_img = models.ImageField(upload_to='slide/',default='placeholders/slide.jpg',blank=True,null=True, verbose_name="Изображение для десктопа")
    mobile_img = models.ImageField(upload_to='slide/',default='placeholders/slide.jpg',blank=True,null=True, verbose_name="Изображение для моб.устройств")

    button1 = models.BooleanField(verbose_name="Нужна ли кнопка 1 (Если галочка не стоит - кнопка отображаться не будет)")
    button1_text = models.CharField(max_length=24, verbose_name="Текст для кнопки 1 (24 зн.)")
    button1_url = models.CharField(max_length=1024, verbose_name="Ссылка для кнопки 1 (1024 зн.)")
    button2 = models.BooleanField(verbose_name="Нужна ли кнопка 2 (Если галочка не стоит - кнопка отображаться не будет)")
    button2_text = models.CharField(max_length=24, verbose_name="Текст для кнопки 2 (24 зн.)")
    button2_url = models.CharField(max_length=1024, verbose_name="Ссылка для кнопки 2 (1024 зн.)")

    def __str__(self):
        return f"Слайд {self.id}"
    
    class Meta():
        verbose_name = "слайд"
        verbose_name_plural = "Слайды"
        ordering = ['id']


class Partners(models.Model):

    img = models.ImageField(upload_to='partners/',default='placeholders/partners.jpg',blank=True, verbose_name="Фотография")

    def __str__(self):
        return f"Изображение партнера {self.id}"
    
    class Meta():
        verbose_name = "партнер"
        verbose_name_plural = "Партнеры"
        ordering = ['-id']
