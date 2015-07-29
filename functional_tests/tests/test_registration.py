from .base import FunctionalTest

class RegistrationTest(FunctionalTest):

    def test_registration(self):

        # user goes to the homepage
        self.browser.get(self.live_server_url)
