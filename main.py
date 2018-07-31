from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
from utils import SessionAction


class ElementarySessionExtension(Extension):
    def __init__(self):
        super(ElementarySessionExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        options = ['lock', 'logout', 'suspend',
                   'sleep', 'restart', 'reboot', 'shutdown', 'power-off', ]
        actions = []
        my_list = event.query.split(" ")
        if len(my_list) == 1:
            actions.append(lock_screen_item())
            actions.append(suspend_item())
            actions.append(reboot_item())
            actions.append(shutdown_item())
            return RenderResultListAction(actions)
        else:
            my_query = my_list[1]
            included = []
            for option in options:
                if my_query in option:
                    if option in ['shutdown', 'power-off'] and 'shutdown' not in included:
                        actions.append(shutdown_item())
                        included.append('shutdown')
                    elif option in ['restart', 'reboot'] and 'reboot' not in included:
                        actions.append(reboot_item())
                        included.append('reboot')
                    elif option in ['suspend', 'sleep'] and 'suspend' not in included:
                        actions.append(suspend_item())
                        included.append('suspend')
                    elif option in ['lock']:
                        actions.append(lock_screen_item())
                        included.append('lock')
                    elif option in ['logout']:
                        actions.append(logout_item())
                        included.append('logout')

            return RenderResultListAction(actions)


def reboot_item():
    return ExtensionResultItem(icon='images/system-reboot.svg',
                               name='Reboot',
                               description='Reboot computer.',
                               on_enter=RunScriptAction(SessionAction.reboot(), None))


def shutdown_item():
    return ExtensionResultItem(icon='images/system-shutdown.svg',
                               name='Shutdown',
                               description='Power off computer.',
                               on_enter=RunScriptAction(SessionAction.power_off(), None))


def lock_screen_item():
    return ExtensionResultItem(icon='images/system-lock-screen.svg',
                               name='Lock',
                               description='Lock screen.',
                               on_enter=RunScriptAction(SessionAction.lock(), None))


def suspend_item():
    return ExtensionResultItem(icon='images/system-suspend.svg',
                               name='Suspend',
                               description='Suspend session.',
                               on_enter=RunScriptAction(SessionAction.suspend(), None))


def logout_item():
    return ExtensionResultItem(icon='images/system-log-out.svg',
                               name='Log Out',
                               description='This will close all open applications.',
                               on_enter=RunScriptAction(SessionAction.logout(), None))


if __name__ == '__main__':
    ElementarySessionExtension().run()
