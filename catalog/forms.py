from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("views_counter", "data_make",)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Политикой платформы запрещена продажа или упоминание: {word}')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Политикой платформы запрещена продажа или упоминание: {word}')

        return cleaned_data


class VersionForm(StyleMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"


class ModeratorForm(StyleMixin, forms, ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')