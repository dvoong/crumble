import pdb
from .base import FunctionalTest
from selenium.webdriver.support.ui import Select

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
        registration_form = RegistrationForm(self.browser)
        registration_form.test(self)
        # the user fills in the fields
        select = Select(registration_form.registration_type.input)
        select.select_by_visible_text('Student')
        registration_form.email.input.send_keys('voong.david@gmail.com')
        registration_form.password.input.send_keys('secret')
        registration_form.confirmation_password.input.send_keys('secret')
        registration_form.submit.click()
        # the user is rent a registration email
        # the user is redirected to a page to fill in their profile
        self.assertEqual(self.browser.current_url, self.live_server_url + '/profile/voong.david@gmail.com')
        
class RegistrationForm:
    def __init__(self, browser):

        self.form = browser.find_element_by_id('registration-form')
        self.registration_type = RegistrationTypeField(self)
        self.email = EmailField(self)
        self.password = PasswordField(self)
        self.confirmation_password = PasswordConfirmationField(self)
        self.fields = [
            self.registration_type,
            self.email,
            self.password,
            self.confirmation_password,
        ]
        self.submit = self.form.find_element_by_css_selector('input[type="submit"]')

    def test(self, test_case):
        for field in self.fields:
            field.test(test_case)

class RegistrationFormField:
    def test(self, test_case):
        self.fail('TODO: Write tests for me')

                
class RegistrationTypeField(RegistrationFormField):
    def __init__(self, registration_form):
        self.label = registration_form.form.find_element_by_css_selector('label[for="id_registration_type"]')
        self.input = registration_form.form.find_element_by_name('registration_type')
            
    def test(self, test_case):
        test_case.assertEqual(self.label.text, 'I am a:')
        test_case.assertEqual(self.input.tag_name, 'select')

                
class EmailField(RegistrationFormField):
    def __init__(self, registration_form):
        self.label = registration_form.form.find_element_by_css_selector('label[for="id_email"]')
        self.input = registration_form.form.find_element_by_name('email')

    def test(self, test_case):
        test_case.assertEqual(self.label.text, 'Email:')
        test_case.assertEqual(self.input.tag_name, 'input')
        test_case.assertEqual(self.input.get_attribute('type'), 'email')
                
                
class PasswordField(RegistrationFormField):
    def __init__(self, registration_form):
        self.label = registration_form.form.find_element_by_css_selector('label[for="id_password"]')
        self.input = registration_form.form.find_element_by_name('password')

    def test(self, test_case):
        test_case.assertEqual(self.label.text, 'Password:')
        test_case.assertEqual(self.input.get_attribute('type'), 'password')
                
class PasswordConfirmationField(RegistrationFormField):
    def __init__(self, registration_form):
        self.label = registration_form.form.find_element_by_css_selector('label[for="id_password_confirmation"]')
        self.input = registration_form.form.find_element_by_name('password_confirmation')

    def test(self, test_case):
        test_case.assertEqual(self.label.text, 'Confirm Password:')
        test_case.assertEqual(self.input.get_attribute('type'), 'password')
