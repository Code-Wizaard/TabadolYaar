from pyrobale import Client
from pyrobale.objects import Message, CallbackQuery
import pyrobale
import os

token = os.getenv("TOKEN")

bot = Client(token)

