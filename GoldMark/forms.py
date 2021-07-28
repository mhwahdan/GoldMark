from django import forms


class SendMessageForm(forms.Form):
    name = forms.CharField(label='name',
                           widget=forms.TextInput(
                            attrs={
                               'class': 'cfos_field required',
                               'placeholder': 'your name',
                               'title': '* Please provide Name',
                               'id': 'cfos-name'
                            }), max_length=20)
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(
                                attrs={
                                    'class': 'cfos_field required',
                                    'placeholder': 'your Email',
                                    'title': '* Please provide Email',
                                    'id': 'cfos-email'
                                })
                             )
    phonenumber = forms.CharField(label='phonenumber',
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'cfos_field',
                                     'placeholder': 'Your Number',
                                     'autocomplete': 'off',
                                     'id': 'cfos-number',
                                     'type': 'tel',
                                 }
                             ),
                             max_length=20,)
    message = forms.CharField(label='Message',
                              widget=forms.Textarea(
                                  attrs={
                                      'cols': 40,
                                      'rows': 6,
                                      'class': 'cfos_text_field required',
                                      'placeholder': 'Tell us about desired property',
                                      'title': '* Please provide Message',
                                      'id': 'cfos-message'
                                  }
                              ),
                              max_length=500,
                              required=True)
    country_code = forms.CharField(required=True, widget=forms.HiddenInput())
