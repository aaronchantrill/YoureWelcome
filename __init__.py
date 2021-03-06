# -*- coding: utf-8 -*-
from naomi import plugin

class Plugin(plugin.SpeechHandlerPlugin):
    def intents(self):
        _ = self.gettext
        return {
            'ThankYouIntent': {
                'locale': {
                    'en-US': {
                        'templates': [
                            "THANK YOU",
                            "THANKS"
                        ]
                    },
                    'fr-FR': {
                        'templates': [
                            "MERCI"
                        ]
                    },
                    'de-DE': {
                        'templates': [
                            "DANKE"
                        ]
                    }
                },
                'action': self.handle
            }
        }

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

    def handle(self, intent, mic):
        mic.say("You are welcome")
