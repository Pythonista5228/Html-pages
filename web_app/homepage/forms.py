from django import forms

class ProductsForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    product_description = forms.CharField()
    product_slug = forms.SlugField()  
    product_price = forms.CharField()
    product_rating = forms.CharField()
    product_quantity = forms.CharField()

    def clean_name(self):
        name = self.cleaned_data['product_name']
        if name == 'djangobin' or name == 'DJANGOBIN':
            raise ValidationError("name can't be {}.".format(name))
 
        # Always return the data
        return name
 
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
 
    def clean(self):
        cleaned_data = super(LanguageForm, self).clean()
        slug = cleaned_data.get('slug')
        mime = cleaned_data.get('mime')
 
        if slug == mime:
            raise ValidationError("Slug and MIME shouldn't be same.")
 
        # Always return the data
        return cleaned_data