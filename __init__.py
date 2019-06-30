# -*- coding: utf-8 -*-
from naomi import plugin

class Plugin(plugin.SpeechHandlerPlugin):

    def is_valid(self, text):
        return self.get_phrases()

    def get_phrases(self):
        return [
            'THANK YOU',
            'THANKS'
        ]

    def handle(self, text, mic):
        self.mic.say("You are welcome")
