from django.forms import ModelForm

from apps.main.models import Product


class ProductCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if str(field) != "is_active":
                self.fields[field].widget.attrs.update(
                    {"class": "form-control", "placeholder": f"Enter the {str(field)}"})

    class Meta:
        model = Product
        fields = '__all__'


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
