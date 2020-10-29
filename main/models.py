from django.db import models
import datetime


class Now(models.Model):
    now = models.DateField(default=datetime.datetime.now())


class User(models.Model):
    username = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username


class Contract(models.Model):
    type = 'Поставки'

    # Общая информация

    date_of_signing = models.DateField('Дата подписания')
    SIDE_CHOICES = [
        ('Поставщик', 'Поставщик'),
        ('Покупатель', 'Покупатель')
    ]
    side = models.CharField(
        'Сторона в договоре',
        max_length=10,
        choices=SIDE_CHOICES,
        default='Покупатель',
    )
    title = models.CharField('Наименование Организации', max_length=200)
    director = models.CharField('Генеральный директор', max_length=100)
    legal_address = models.CharField('Адрес', max_length=254)
    email = models.EmailField('E-mail', max_length=200)
    number_of_contract = models.CharField('Номер договора', max_length=250)

    # Условия Договора
    # Предмет логовора
    terms = models.TextField('Содержание работ', null=True)
    # Порядок исполнения

    # Предмет договора:
    # Открытие кнопка 'Выбрать' списка работы/услуги
    name = models.CharField('Наименование', max_length=120)
    amount = models.IntegerField('Количество')

    # Загрузить текст
    file = models.FileField('Прикрепленный файл', blank=True, upload_to='static/uploads/%Y/%m/%d/')

    period_of_execution = models.DateField('Срок выполнения')

    # Automate
    date_of_creation = models.DateField('Дата создания', auto_now_add=True)

    PAYMENT = 'На этапе оплаты'
    SIGNING = 'На этапе подписывания'
    STATUS_CHOICES = [
        (PAYMENT, 'На этапе оплаты'),
        (SIGNING, 'На этапе подписывания')
    ]
    status = models.CharField(
        'Статус',
        max_length=21,
        choices=STATUS_CHOICES,
        default=SIGNING,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class Events(models.Model):
    title = models.CharField('Задача', max_length=90)
    date = models.DateField('Срок выполнения')
    commentary = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Точка контроля'
        verbose_name_plural = 'Точки контроля'


class Timing(models.Model):
    DONE = 'Выполнено'
    NOT_DONE = 'Не выполнено'
    REACTION_CHOICES = [
        (DONE, 'Выполнено'),
        (NOT_DONE, 'Не выполнено')
    ]

    contract = models.ForeignKey(Contract, null=True, on_delete=models.SET_NULL)

    execution_period = models.DateField('Срок исполнения')
    subject = models.IntegerField('Количество обещанного товара')
    payment_period = models.DateField('Срок оплаты')

    reaction = models.CharField(
        'Реакция',
        max_length=12,
        choices=REACTION_CHOICES,
        default=NOT_DONE,
    )

    amount = models.DecimalField('Сумма', max_digits=15, decimal_places=2, default=0.00)
    days = models.IntegerField('Дни разницы', default=0)  # от 0 до 32767
    penalty = models.DecimalField('Неустойка', max_digits=15, decimal_places=2, default=0.00)
    paid = models.DecimalField('Заплачено', max_digits=15, decimal_places=2, default=0.00)
    delivered = models.IntegerField('Доставлено', default=0)

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Срок'
        verbose_name_plural = 'Сроки'
