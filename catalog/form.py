from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from catalog.models import Product, Version

class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("views_counter",)

        def clean_name(self):
            name = self.cleaned_data["name"]
            forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                               'радар']
            for word in forbidden_words:
                if word in name.lower():
                    raise ValidationError(f'Название продукта содержит запрещенное слово: {word}')
            return name

        def clean_description(self):
            description = self.cleaned_data.get('description')
            forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                               'радар']
            for word in forbidden_words:
                if word in description.lower():
                    raise ValidationError(f'Описание продукта содержит запрещенное слово: {word}')
            return description

class VersionForm(StyleMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"