from django.db import models

# arMA7272AR

class Member(models.Model):

    job = models.CharField(max_length=255, verbose_name="Должность 255зн.")
    name = models.CharField(max_length=255, verbose_name="Имя и Фамилия 255зн.")
    des = models.CharField(max_length=511, verbose_name="Описание 511зн.")
    img = models.ImageField(upload_to='members/',default='placeholders/placeholder.jpg',blank=True,null=True, verbose_name="Фотография (исключительно квадратные)")
    
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "члена команды"
        verbose_name_plural = "Члены команды"
        ordering = ['name']

class News(models.Model):

    img = models.ImageField(upload_to='news/',default='placeholders/news.jpg',blank=True,null=True, verbose_name="Фотография 1596x500")

    def __str__(self):
        return f"Новость {self.id}"
    
    class Meta():
        verbose_name = "новость"
        verbose_name_plural = "Новости"
        ordering = ['-id']

class Partners(models.Model):

    img = models.ImageField(upload_to='partners/',default='placeholders/partners.jpg',blank=True, verbose_name="Фотография")

    def __str__(self):
        return f"Изображение партнера {self.id}"
    
    class Meta():
        verbose_name = "партнер"
        verbose_name_plural = "Партнеры"
        ordering = ['-id']
