import urllib
import logging

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

LOGGER = logging.getLogger(__name__)

def urlencode(q):
    return urllib.urlencode(q)

class LingueeExtension(Extension):

    def __init__(self):
        super(LingueeExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = list()

        if event.get_argument():
            LOGGER.info('Word Linguee search for "{}"'.format(event.get_argument()))
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Define words on Linguee',
                    description='Define words "{}".'.format(event.get_argument()),
                    on_enter=OpenUrlAction(
                        'https://www.linguee.com/english-french/search?{}'.format(urlencode({ 'source': 'auto', 'query': event.get_argument() }))
                    )
                )
            )

        return RenderResultListAction(items)

if __name__ == '__main__':
    LingueeExtension().run()
