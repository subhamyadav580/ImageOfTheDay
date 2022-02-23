from django import forms
from .models import FeaturedImage

class ImageUploadForm(forms.ModelForm):

	class Meta:
		model = FeaturedImage
		fields = ['name', 'tagline', 'img']
