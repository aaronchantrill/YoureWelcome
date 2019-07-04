# -*- coding: utf-8 -*-
from naomi import plugin

class Plugin(plugin.SpeechHandlerPlugin):

    def is_valid(self, text):
        """
        Returns True to trigger handle.

        Arguments:
        text -- user-input, typically transcribed speech
        """
        return any(
            (phrase.upper() in text.upper())
            for phrase in self.get_phrases()
        )

    def get_phrases(self):
        return [
            'THANK YOU',
            'THANKS'
        ]

    def handle(self, text, mic):
        mic.say("You are welcome")
