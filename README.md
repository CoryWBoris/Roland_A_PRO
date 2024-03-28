# Pause Button Functionality Added To Roland A Pro Series For Ableton!
![Stability Badge](https://img.shields.io/badge/-stable-blue)  
## Steps to install - Note: these are not the same as the user library's remote scripts. Pay attention carefully to your directory:
1. Go here  
   a.) On Mac: `/Applications/Ableton Live 11/Contents/App-Resources/MIDI Remote Scripts/Roland_A_PRO`  
   b.) On Windows: `C:\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts\Roland_A_PRO`
3. Rename the Roland_A_PRO.pyc file something like Roland_A_PRO_Original.pyc, and put it in a folder so it is safe.
4. Replace Roland_A_PRO.pyc in the Roland_A_PRO folder with this Roland_A_PRO.py file
5. Restart Ableton or open Ableton if not open

## Use of Pause Button for Roland A Pro Series:
Enjoy a pause button! This script allows the pause button which is midi CC 27 on the Roland A Pro series to stop and continue where playing just like a real pause button! Also, sit back and enjoy some ice cream for the time you saved from hitting the stop button or pressing spacebar and shift!    

## How the pause button works:  
If playing and not recording, this button will pause, and play as expected.  
If playing and recording, this button will pause, keeping the recording enabled, and on play, you will still record.  
If you have the 'Start Playback with Record' setting enabled, the pause button works the same.

## If you want to add this functionality to a midi device other than a Roland A PRO synth supported by Ableton with a python based remote script:  
**Note: The scripts in this repo are only intended for Roland A PRO Series and so always backup if you are experiementing with anything. These particular scripts in this repo are robust and have been even improved from their original scripts. But I can't make any claims about any other non Roland A PRO synths at this time.**  
Find your synth's MIDI remote script from this external repo link: https://github.com/gluon/AbletonLive10.1_MIDIRemoteScripts/tree/master  
I understand this particular link is using MIDI Remote Scripts from Ableton 10.1, but I don't believe much has changed from these scripts at the external repo and these are more reliable than the ones available on github for Ableton 11 that I tried out. Basically, in order to create the uncompiled python for these scripts, some fine folks have taken the liberty of decompiling the scripts that came with Ableton. GPT can definitely help you answer questions about these libraries if you get stuck, as they are often enigmatic with google searches and stack overflow providing few examples of this code.  

Simply find out what CC number your device's pause button is, or just assign the CC of any button that is a momentary button -not a toggle button- and replace CC 27 in my script with the actual CC number. The only code you need to add to your default MIDI Remote Script is this:  

While inside the name of the script which matches the name of your folder as it pertains to your specific midi instrument i.e. if you are in the Roland_A_PRO folder, go to the Roland_A_PRO.py file:  

add to the _create_controls method:  

        self._pause_button = ButtonElement(True, MIDI_CC_TYPE, 0, 27)
        self._pause_button.add_value_listener(self._toggle_play_state)  
        
and then add this method inside the class of the name of your MIDI Remote Script:  

    # How to add a pause button
    def _toggle_play_state(self, value):
        if value != 0:  # Ignore button release events
            if self.song().is_playing:
                if self.song().record_mode:
                    # If playing and recording, stop playing and start recording again
                    self.song().stop_playing()
                    self.song().record_mode = True
                else:
                    # If playing and not recording, stop
                    self.song().stop_playing()
            else:
                # If stopped, start where left off
                self.song().continue_playing()

You may have noticed I also included a MixerComponent.py file to this repo. This is because I fixed an index out of bounds bug which hasn't been patched by Ableton yet. It is fixed when replacing the stock MixerComponent.pyc file with this MixerComponent.py file AND replacing the stock Roland_A_PRO.pyc file with my Roland_A_PRO.py script.

Oh, and I don't have the functionality yet which let's you click anywhere and change where the pause button starts from right now. The pause button appears to be very religious about starting from the last spot you played. So as such, you will have to press play on a new spot if you would like that new spot to be where your pause button starts from.

Enjoy being a Pause-Button-Baller®

**Coffees Welcome!**
- <a href="https://coryboris.gumroad.com/l/TrueAutoColor">TrueAutoColor</a>
- Paypal: tromboris@gmail.com
- Venmo: @Cory-Boris
- Ethereum Address: `0x3f6af994201c17eF1E86ff057AB2a2F6CB0D1f6a`

Thank you! 🔥🥰✌🏻🙏🏻

**Happy Music Making,**  
-C
