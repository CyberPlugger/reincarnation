from __future__ import annotations

def own(name):
    return type(name, (Exception,), {})

exc_list = {
    'main_exc': own('MainException'),
    'reincarnated': own('ReincarnationException'),
    'UnknownException': own('UnknownException')
}