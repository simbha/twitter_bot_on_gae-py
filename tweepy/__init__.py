# Tweepy
# Copyright 2009 Joshua Roesslein
# See LICENSE

"""
Tweepy Twitter API library
"""
__version__ = '1.1'

from . models import Status, User, DirectMessage, Friendship, SavedSearch, SearchResult, models
from . error import TweepError
from . api import API
from . cache import Cache, MemoryCache, FileCache, MemCache
from . auth import BasicAuthHandler, OAuthHandler
from . streaming import Stream, StreamListener
from . logging import TweepyLogger, DummyLogger, ConsoleLogger, FileLogger
from . cursor import Cursor

# Global, unauthenticated instance of API
api = API()

