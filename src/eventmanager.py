from weakref import WeakKeyDictionary

import events
import events as ev


class EventManager:
    def __init__(self):
        self.listeners = WeakKeyDictionary()

    def register_listener(self, listener):
        """
        Adds a listener to call list.
        It will receive post() events though it's notify(event) call.
        """

        self.listeners[listener] = 1

    def unregister_listener(self, listener):

        """
         Remove a listener from our spam list.
         Our weak ref spam list will auto remove any listeners who stop existing.
        """

        if listener in self.listeners:
            del self.listeners[listener]

    def post(self, event):

        """
        post a new event to message queue, event will be broadcast to all listeners
        """

        if not isinstance(event, events.TickEvent) and not isinstance(event, events.MouseMoveEvent):
            # print the event (unless it is TickEvent or MouseMove)
            print(str(event))
        for listener in list(self.listeners):
            listener.notify(event)
