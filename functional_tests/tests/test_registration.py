from .base import FunctionalTest

class RegistrationTest(FunctionalTest):
    
    def test_registration(self):

        # user goes to the homepage
        self.browser.get(self.live_server_url)
        # user clicks on a link to register
        registration_link = self.browser.find_element_by_link_text("Register")
        registration_link.click()
        # user is sent to the registration page
        self.assertEqual(self.browser.current_url, self.live_server_url + '/registration')
        self.assertEqual(self.browser.title, 'Registration')
        # the page has a form
        registration_form = self.RegistrationForm(self.browser)
        registration_form.test(self)
        
    class RegistrationForm:
        def __init__(self, browser):

            self.form = browser.find_element_by_id('registration-form')
            self.fields = [
                RegistrationTypeField(self),
                EmailField(self),
                PasswordField(self),
                PasswordConfirmationField(self)
            ]

        def test(self, test_case):
            for field in self.fields:
                field.test(test_case)

        class RegistrationFormField:
            def test(self, test_case):
                self.fail('TODO: Write tests for me')

                
        class RegistrationTypeField(RegistrationFormField):
            def __init__(self, registration_form):
                self.label = registration_form.form.find_element_by_css_selector('label[for="registration-type"]')
                self.input = registration_form.form.find_element_by_name('registration-type')

            def test(self, test_case):
                test_case.assertEqual(self.label.text, 'I am a:')
                test_case.assertEqual(self.input.tag_name, 'select')

                
        class EmailField(RegistrationFormField):
            def __init__(self, registration_form):
                self.label = registration_form.form.find_element_by_css_selector('label[for="email"]')
                self.input = registration_form.form.find_element_by_name('email')

            def test(self, test_case):
                test_case.assertEqual(self.label.text, 'Email:')
                test_case.assertEqual(self.input.tag_name, 'input')
                test_case.assertEqual(self.input.get_attribute('type'), 'email')
                
                
        class PasswordField(RegistrationFormField):
            def __init__(self, registration_form):
                self.label = registration_form.form.find_element_by_css_selector('label[for="password"]')
                self.input = registration_form.form.find_element_by_name('password')

            def test(self, test_case):
                test_case.assertEqual(self.label.text, 'Password:')
                test_case.assertEqual(self.input.get_attribute('type'), 'password')
                
        class PasswordConfirmationField(RegistrationFormField):
            def __init__(self, registration_form):
                self.label = registration_form.form.find_element_by_css_selector('label[for="password-confirmation"]')
                self.input = registration_form.form.find_element_by_name('password-confirmation')

            def test(self, test_case):
                test_case.assertEqual(self.label.text, 'Confirm Password:')
                test_case.assertEqual(self.input.get_attribute('type'), 'password')
