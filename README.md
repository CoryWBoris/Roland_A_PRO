## Pause Button Functionality Added To Roland A Pro Series For Ableton

## Steps - Note: these are not the same as user library's remote scrips. Pay attention carefully to your directory:
1. Go here  
   a.) On Mac: `/Applications/Ableton Live 11/Contents/App-Resources/MIDI Remote Scripts/Roland_A_PRO`  
   b.) On Windows: `C:\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts\Roland_A_PRO`
3. Replace Roland_A_PRO.pyc with this Roland_A_PRO.py file
4. Restart Ableton or open Ableton if not open

Enjoy a pause button! This script allows the pause button which is midi CC 27 on the Roland A Pro series to stop and continue where playing just like a pause button.  

Also, if you want to do this to your own synth, find your synth's MIDI remote script from this repo: https://github.com/gluon/AbletonLive10.1_MIDIRemoteScripts/tree/master  
I understand this is using MIDI Remote Scripts from Ableton 10.1, but not much has changed and these are more reliable than the ones available on github for Ableton 11. Basically, in order to create the uncompiled python for these scripts, some fine folks have taken the liberty of decompiling the scripts that came with Ableton. GPT can definitely help you answer questions about these libraries if you get stuck.  

Simply find out what CC number your device's pause button is, or just assign the CC of any button that is a momentary button -not a toggle button- and replace CC 27 in my script with the actual CC number. The only code you need to add to your default MIDI Remote Script is this:  

add to the _create_controls method:  

        self._pause_button = ButtonElement(True, MIDI_CC_TYPE, 0, 27)
        self._pause_button.add_value_listener(self._toggle_play_state)  
        
and then add this method inside the class of the name of your MIDI Remote Script:  

    # How to add a play button to any MIDI Remote Script
    def _toggle_play_state(self, value):
        if value != 0:  # Ignore button release events
            if self.song().is_playing:
                self.song().stop_playing()
            else:
                self.song().continue_playing()

