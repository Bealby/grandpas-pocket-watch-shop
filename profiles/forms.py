from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        # Telling Django which model it will be associated with and the fields to render. 
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        # Inserted placeholders. Removed auto-generated lables and set auto focus for curser to start on Full Name field
        # Add placeholders and classes, remove auto-generated
        # labels and set autofocus on first field
        super().__init__(*args, **kwargs)
        placeholders = {
            # For better UI on webpage
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Iterate through form fieldsand ading a * to placeholder if required
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black round-0 profile-form-input'
            self.fields[field].label = False
