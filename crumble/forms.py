from crumble.models import User
import django.forms

class RegistrationForm(django.forms.Form):
    email = django.forms.EmailField(label='Email:', max_length=100)
    registration_type = django.forms.ChoiceField(label='I am a:', choices=(('STUDENT', 'Student'), ('COMPANY', 'Company')))
    password = django.forms.CharField(widget=django.forms.PasswordInput)
    password_confirmation = django.forms.CharField(label='Confirm Password:', widget=django.forms.PasswordInput)

    def save(self):
        user = User(
            account_type=self.data['registration_type'],
            email=self.data['email'],
            password=self.data['password']
        )
        user.save()
        return user


    # class RegistrationForm:
    #     def __init__(self, browser):

    #         self.form = browser.find_element_by_id('registration-form')
    #         self.fields = [
    #             RegistrationTypeField(self),
    #             EmailField(self),
    #             PasswordField(self),
    #             PasswordConfirmationField(self)
    #         ]

    #     def test(self, test_case):
    #         for field in self.fields:
    #             field.test(test_case)

    #     class RegistrationFormField:
    #         def test(self, test_case):
    #             self.fail('TODO: Write tests for me')

                
    #     class RegistrationTypeField(RegistrationFormField):
    #         def __init__(self, registration_form):
    #             self.label = registration_form.form.find_element_by_css_selector('label[for="registration-type"]')
    #             self.input = registration_form.form.find_element_by_name('registration-type')

    #         def test(self, test_case):
    #             test_case.assertEqual(self.label.text, 'I am a:')
    #             test_case.assertEqual(self.input.tag_name, 'select')

                
    #     class EmailField(RegistrationFormField):
    #         def __init__(self, registration_form):
    #             self.label = registration_form.form.find_element_by_css_selector('label[for="email"]')
    #             self.input = registration_form.form.find_element_by_name('email')

    #         def test(self, test_case):
    #             test_case.assertEqual(self.label.text, 'Email:')
    #             test_case.assertEqual(self.input.tag_name, 'input')
    #             test_case.assertEqual(self.input.get_attribute('type'), 'email')
                
                
    #     class PasswordField(RegistrationFormField):
    #         def __init__(self, registration_form):
    #             self.label = registration_form.form.find_element_by_css_selector('label[for="password"]')
    #             self.input = registration_form.form.find_element_by_name('password')

    #         def test(self, test_case):
    #             test_case.assertEqual(self.label.text, 'Password:')
    #             test_case.assertEqual(self.input.get_attribute('type'), 'password')
                
    #     class PasswordConfirmationField(RegistrationFormField):
    #         def __init__(self, registration_form):
    #             self.label = registration_form.form.find_element_by_css_selector('label[for="password-confirmation"]')
    #             self.input = registration_form.form.find_element_by_name('password-confirmation')

    #         def test(self, test_case):
    #             test_case.assertEqual(self.label.text, 'Confirm Password:')
    #             test_case.assertEqual(self.input.get_attribute('type'), 'password')
