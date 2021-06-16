from mycroft import MycroftSkill, intent_file_handler


class TexasFacts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('facts.texas.intent')
    def handle_facts_texas(self, message):
        self.speak_dialog('facts.texas')


def create_skill():
    return TexasFacts()

