from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Control import ButtonControl
from _Framework.MixerComponent import MixerComponent as MixerComponentBase

class MixerComponent(MixerComponentBase):
    bank_up_button = ButtonControl()
    bank_down_button = ButtonControl()
    track_up_button = ButtonControl()
    track_down_button = ButtonControl()

    def __init__(self, *a, **k):
        super(MixerComponent, self).__init__(*a, **k)
        self.sends = [] # Initialize sends with None

    @bank_up_button.pressed
    def bank_up_button_pressed(self, button):
        new_offset = self._track_offset + len(self._channel_strips)
        if len(self.tracks_to_use()) > new_offset:
            self.set_track_offset(new_offset)

    @bank_down_button.pressed
    def bank_down_button_pressed(self, button):
        self.set_track_offset(max(0, self._track_offset - len(self._channel_strips)))

    @track_up_button.pressed
    def track_up_button_pressed(self, button):
        new_offset = self._track_offset + 1
        if len(self.tracks_to_use()) > new_offset:
            self.set_track_offset(new_offset)

    @track_down_button.pressed
    def track_down_button_pressed(self, button):
        self.set_track_offset(max(0, self._track_offset - 1))

    # This function didn't exist, and led to an index out of bounds error when selecting certain toggle keys on the physical Roland A PRO Series midi keyboard
    def set_send(self, index, send):
        if 0 <= index < len(self.sends):
            self.sends[index] = send
