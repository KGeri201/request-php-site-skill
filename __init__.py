from mycroft import MycroftSkill, intent_file_handler


class RequestPhpSite(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('site.php.request.intent')
    def handle_site_php_request(self, message):
        self.speak_dialog('site.php.request')


def create_skill():
    return RequestPhpSite()

