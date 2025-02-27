from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband, Women


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else 'Только русские символы'

    def __call__(self, value):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана',label="Категория")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Не замужем', required=False, label="Муж")

    class Meta:
        model = Women
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'})
        }
        labels = {
            'slug': 'URL',
            'cat': 'Категория',}


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Выберите файл')