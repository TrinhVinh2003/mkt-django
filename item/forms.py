from .models import Item
from django import forms

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class Itemclass(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image')
    
        widgets = {
            'category' : forms.Select(attrs={
                'class':INPUT_CLASSES            
            }),
            'name' : forms.TextInput(attrs={
                'class':INPUT_CLASSES            
            }),
            'description' : forms.Textarea(attrs={
                'class':INPUT_CLASSES            
            }),
            
            'price' : forms.TextInput(attrs={
                'class':INPUT_CLASSES            
            }),
            
            'image' : forms.FileInput(attrs={
                'class':INPUT_CLASSES            
            }),
        }
class EditItemclass(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','price','image','is_sold')
    
        widgets = {
            'name' : forms.TextInput(attrs={
                'class':INPUT_CLASSES            
            }),
            'description' : forms.Textarea(attrs={
                'class':INPUT_CLASSES            
            }),
            
            'price' : forms.TextInput(attrs={
                'class':INPUT_CLASSES            
            }),
            
            'image' : forms.FileInput(attrs={
                'class':INPUT_CLASSES            
            }),
            
        }
