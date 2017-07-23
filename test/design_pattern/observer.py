#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: observer.py
@time: 2017/6/12 下午6:06
"""


class AbstractSubject(object):
    def register(self, listener):
        raise NotImplementedError("Must subclass me")

    def de_register(self, listener):
        raise NotImplementedError("Must subclass me")

    def notify_listeners(self, event):
        raise NotImplementedError("Must subclass me")


class Listener(object):
    def __init__(self, name, subject):
        self.name = name
        subject.register(self)

    def notify(self, event):
        print self.name, "received event", event


class Subject(AbstractSubject):
    def __init__(self):
        self.listeners = []
        self.data = None

    def get_user_action(self):
        self.data = raw_input('Enter something to do:')
        return self.data

    # Implement abstract Class AbstractSubject

    def register(self, listener):
        self.listeners.append(listener)

    def de_register(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self, event):
        for listener in self.listeners:
            listener.notify(event)


if __name__ == "__main__":
    # make a subject object to spy on
    subject_obj = Subject()

    # register two listeners to monitor it.
    listenerA = Listener("<listener A>", subject_obj)
    listenerB = Listener("<listener B>", subject_obj)

    # simulated event
    subject_obj.notify_listeners("<event 1>")
    # outputs:
    #     <listener A> received event <event 1>
    #     <listener B> received event <event 1>

    action = subject_obj.get_user_action()
    subject_obj.notify_listeners(action)
    # Enter something to do:hello
    # outputs:
    #     <listener A> received event hello
    #     <listener B> received event hello


# https://zh.wikipedia.org/wiki/观察者模式