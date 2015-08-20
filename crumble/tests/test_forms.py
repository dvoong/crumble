import mock
import django.test
import crumble.forms

class CrumbleFormTest(django.test.TestCase):

    pass

@mock.patch('crumble.forms.User')
class RegistrationFormTest(CrumbleFormTest):

    def setUp(self):
        self.form = crumble.forms.RegistrationForm(
            data={'email': 'abc@abc.com',
                  'password': 'secret',
                  'registration_type': 'STUDENT',
                  'password_confirmation': 'secret',
            })

    def test_save_returns_a_user_object(self, mock_User):
        user = mock.Mock()
        mock_User.return_value = user

        output = self.form.save()

        self.assertEqual(output, user)

    def test_save_creates_user(self, mock_User):

        self.form.save()

        mock_User.assert_called_once_with(email=self.form.data['email'],
                                          password=self.form.data['password'],
                                          account_type=self.form.data['registration_type'])


    def test_save_saves_user_to_db(self, mock_User):

        user = self.form.save()

        user.save.assert_called_once_with()

    
