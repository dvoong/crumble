import mock
import django.test
import crumble.views
from django.core.urlresolvers import resolve as resolve_url

class CrumbleViewTest(django.test.TestCase):

    pass

class RegistrationViewTest(CrumbleViewTest):

    def test_url_resolves_to_view(self):
        found = resolve_url('/registration')
        self.assertEqual(found.func, crumble.views.registration)

    @mock.patch('crumble.forms.RegistrationForm')
    @mock.patch('crumble.views.render')
    def test_view_renders_registration_template(self, mock_render, mock_RegistrationForm):
        request = mock.Mock()
        request.method = 'GET'
        registration_form = mock_RegistrationForm()
        crumble.views.registration(request)
        mock_render.assert_called_once_with(request, 'crumble/registration.html', {'registration_form': registration_form})

    @mock.patch('crumble.forms.RegistrationForm')
    @mock.patch('crumble.views.redirect')
    def test_post_redirects_to_new_users_profile_page_if_the_form_is_valid(self, mock_redirect, mock_RegistrationForm):
        request = mock.Mock()
        request.method = 'POST'
        request.POST = {'email': 'voong.david@gmail.com'}
        request.META = {}
        registration_form = mock.Mock(is_vaild=mock.Mock(return_value=True))
        user = mock.Mock(email=request.POST['email'], homepage='/profile/{}'.format(request.POST['email']))
        registration_form.save = mock.Mock(return_value=user)
        mock_RegistrationForm.return_value = registration_form

        crumble.views.registration(request)

        registration_form.is_valid.assert_called_once_with()
        mock_redirect.assert_called_once_with(user.homepage)

        
