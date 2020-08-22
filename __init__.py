from mycroft import MycroftSkill, intent_file_handler
import requests

class RequestPhpSite(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('site.php.request.intent')
    def handle_site_php_request(self, message):
        try:
          url = self.settings.get('url')
          username = self.settings.get('username')
          password = self.settings.get('password')
          requests.post(url, auth=(username, password))
          self.speak_dialog('site.php.request')
        except:
          self.speak_dialog('error')


def create_skill():
    return RequestPhpSite()

