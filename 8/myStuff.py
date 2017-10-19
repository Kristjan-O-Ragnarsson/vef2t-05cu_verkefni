"""
Kristjan O.
myStuff 0.1.x
"""

DEBUG = True
PORT = 81
HOST = 'localhost'


session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': True,
    'session.auto': True
}


def debug(*args, **kwargs):
    if DEBUG:
        print(args, kwargs)


def msg(msg, title):
    """ a msg page for bottle """
    return None#template()
