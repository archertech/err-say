from errbot import BotPlugin, botcmd
import re

class SayBot(BotPlugin):

    @botcmd(split_args_with=":", admin_only=True)
    def say(self, mess, args):
        """A command that lets you tell the bot what to say on a channel"""

        if len(args) < 2:
          yield "I don't understand what you meant."
        else:
          self.send(self.build_identifier(args[0]), ' '.join(args[1:]))
