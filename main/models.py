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

    desktop_img = models.ImageField(upload_to='slide/',default='placeholders/slide.jpg',blank=True,null=True, verbose_name="Изображение для десктопа 2354х1002 .png")
    mobile_img = models.ImageField(upload_to='slide/',default='placeholders/slide.jpg',blank=True,null=True, verbose_name="Изображение для моб.устройств 766х892 .png")

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
        
class AboutUsSlide(models.Model):

    img = models.ImageField(upload_to='partners/',default='placeholders/aboutusslide.jpg',blank=True, verbose_name="Слайд")

    def __str__(self):
        return f"Слайд (о нас) {self.id}"
    
    class Meta():
        verbose_name = "слайд (о нас)"
        verbose_name_plural = "Слайды (о нас)"
        ordering = ['id']

class Partners(models.Model):

    img = models.ImageField(upload_to='partners/',default='placeholders/partners.jpg',blank=True, verbose_name="Изображение партнера")

    def __str__(self):
        return f"Изображение партнера {self.id}"
    
    class Meta():
        verbose_name = "партнер"
        verbose_name_plural = "Партнеры"
        ordering = ['-id']

class Manufactory(models.Model):

    start_time = models.CharField(max_length=24, verbose_name="Время начала. Например 10:00 (24 зн.)")
    finish_time = models.CharField(max_length=24, verbose_name="Время конца. Например 22:00 (24 зн.)")
    utc_text = models.CharField(max_length=56, verbose_name="Часовой пояс. Например 'По московскому времени' (56 зн.)")
    city = models.CharField(max_length=56, verbose_name="Город. Например 'г. Москва' (56 зн.)")
    address = models.CharField(max_length=128, verbose_name="Адрес. Например 'ул. Краснобогатырская 2, стр. 4' (128 зн.)")
    contacts = models.CharField(max_length=56, verbose_name="Контакты. Например '+7 9999 - 623 - 469' (56 зн.)")

    def __str__(self):
        return f"Цех {self.id}"
    
    class Meta():
        verbose_name = "цех"
        verbose_name_plural = "Цеха"
        ordering = ['id']

class SiteConfiguration(models.Model):

    phone = models.CharField(max_length=56, verbose_name="Номер телефона")
    email = models.CharField(max_length=128, verbose_name="Почта")
    telegram = models.CharField(max_length=128, verbose_name="Телеграм")
    whatsapp = models.CharField(max_length=128, verbose_name="Ватсап")
    vk = models.CharField(max_length=128, verbose_name="Вк")
    inn = models.CharField(max_length=128, verbose_name="ИНН")
    ogrn = models.CharField(max_length=128, verbose_name="ОГРН")
    yandex = models.CharField(max_length=512, verbose_name="Ссылка на местоположение (Яндекс.Карты)")

    def __str__(self):
        return f"Конфигурация {self.id}"
    
    class Meta():
        verbose_name = "конфигурацию"
        verbose_name_plural = "Конфигурация сайта"
        ordering = ['id']