# -*- coding: utf-8 -*-
# Part of KamelChaker. See LICENSE file for full copyright and licensing details.

from threading import Event
import time


class EventManager(object):
    def __init__(self):
        self.sessions = {}

    def _delete_expired_sessions(self, max_time=70):
        '''
        Clears sessions that are no longer called.

        :param max_time: time a session can stay unused before being deleted
        '''
        now = time.time()
        expired_sessions = [
            session
            for session in self.sessions
            if now - self.sessions[session]['time_request'] > max_time
        ]
        for session in expired_sessions:
            del self.sessions[session]

    def add_request(self, listener):
        self.session = {
            'session_id': listener['session_id'],
            'devices': listener['devices'],
            'event': Event(),
            'result': {},
            'time_request': time.time(),
        }
        self._delete_expired_sessions()
        self.sessions[listener['session_id']] = self.session
        return self.sessions[listener['session_id']]

    def device_changed(self, device):
        for session in self.sessions:
            if device.device_identifier in self.sessions[session]['devices']:
                self.sessions[session]['result'] = device.data
                self.sessions[session]['result']['device_identifier'] = device.device_identifier
                self.sessions[session]['event'].set()


event_manager = EventManager()
