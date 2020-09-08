#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The :mod:`ml_research_toolkit.notifications.telegram_client` contains classes:
- :class:`ml_research_toolkit.notifications.telegram_client.TelegramUpdaterSingleton`
- :class:`ml_research_toolkit.notifications.telegram_client.TelegramClient`
"""
from __future__ import print_function

__docformat__ = 'restructuredtext'

from telegram.ext import Updater
from telegram.ext import CommandHandler

class TelegramUpdaterSingleton(object):
    r"""
    Singleton class to prevent error while one Telegram updater load twice.
    """
    _updater = dict()

    @staticmethod
    def get(token):
        r"""
        :return: returns updater which related to given token
        :rtype: telegram.ext.Updater
        """
        if token not in TelegramUpdaterSingleton._updater:
            TelegramUpdaterSingleton._updater[token] = Updater(token=token, use_context=True)
            
        TelegramUpdaterSingleton._updater[token].stop()
        list_of_handler = []
        for group in TelegramUpdaterSingleton._updater[token].dispatcher.handlers:
            for item in TelegramUpdaterSingleton._updater[token].dispatcher.handlers[group]:
                list_of_handler.append((group, item))
                
        for group, item in list_of_handler:
            TelegramUpdaterSingleton._updater[token].dispatcher.remove_handler(item, group)

        return TelegramUpdaterSingleton._updater[token]



class TelegramClient(object):
    r"""
    Class for notification sender to telegram.
    """
    def __init__(self, token=None, name=None):
        if token is None:
            raise ValueError('token must be specified')
            
        self.name = name
        
        self.updater = TelegramUpdaterSingleton.get(token)
        self.dispatcher = self.updater.dispatcher
        
        self.dispatcher.add_handler(CommandHandler('start', lambda x,y: self._start(x,y)))
        self.dispatcher.add_handler(CommandHandler('stop', lambda x,y: self._stop(x,y)))
        
        self.updater.start_polling(clean=True)
        
        self._curent_chat_ids = set()
        
    def _start(self, update, context):
        self._curent_chat_ids.add(update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Start tracking: {}".format(str(self.name)))
        
    def _stop(self, update, context):
        if update.effective_chat.id in self._curent_chat_ids:
            self._curent_chat_ids.remove(update.effective_chat.id)
            context.bot.send_message(chat_id=update.effective_chat.id, text="Stop tracking: {}".format(str(self.name)))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Already not tracking: {}".format(str(self.name)))
        
    def send_text(self, text):
        r"""
        Sent simple text message to telegram.

        :param text: message to send
        :type text: str
        """
        for chat_id in self._curent_chat_ids:
            self.updater.bot.send_message(chat_id, text)
    