from errbot import BotPlugin, botcmd
import re

class SayBot(BotPlugin):

    @botcmd(split_args_with=":", admin_only=True)
    def say(self, mess, args):
        """A command that lets you tell the bot what to say on a channel"""

        self.send(args[0], args[1], message_type="groupchat")
