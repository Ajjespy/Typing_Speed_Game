from arcade import Sound
import time

SOUND_VOLUME = .2
FADE_RATE = SOUND_VOLUME * 0.1
SFX_VOLUME = 1


class SoundHandler(Sound):
    """Plays and modifies sounds and music"""
    def __init__(self, index=0) -> None:
        
        self.current_sound_index = index

        self.sound_list = None
        self.sound = None
        self.volume = SOUND_VOLUME
        self.current_player = None

        self.fading = False


    def update_sound_list(self, sound_list) -> None:
        """Updates list of songs and sound effects.
            Parameters: 
                sound_list: list - takes a list of file paths to sound files"""
        self.sound_list = sound_list

    def advance_song(self) -> None:
        """Advance our pointer to the next song. Not used when music loops or same
           effect is used."""
        self.current_sound_index += 1
        if self.current_sound_index >= len(self._list):
            self.current_sound_index = 0


    def get_stream_position(self, player) -> float:
        """Returns position in the sound file in seconds. Resets to 0.0 when sound finishes."""
        return super().get_stream_position(self.current_player)

    def play_song(self) -> None:
        """ Plays song. """
        
        # print('started track')
        # if self.sound and self.sound.is_playing(self.current_player):  # Stop what is currently playing.
        #     print('fading')
        #     self.fade_song()
        #     # return

        if len(self.sound_list) == 0:
            self.stop()
            return

        if self.sound:
            self.sound.stop(self.current_player)

        # Play the next song
        self.sound = Sound(self.sound_list[self.current_sound_index], streaming=True)
        self.current_player = self.sound.play(self.volume)
        # Small delay so the function doesn't skip a track
        time.sleep(0.03)

    
    def change_song(self) -> None:  # TODO This does not work. ⊙﹏⊙∥
        self.sound.stop(self.current_player)
        self.play_song()


    def fade_song(self) -> None:  # TODO This does not work. ⊙﹏⊙∥
        """Fades the music out for screen transitions."""
        self.fading = True
        volume = self.sound.get_volume(self.current_player)

        while volume > 0:
            volume -= FADE_RATE
            print(round(volume, 2))
            self.sound.set_volume(round(volume, 2), self.current_player)

        if volume <= 0:
            self.change_song()

    def stop(self) -> None:
        return super().stop(self.current_player)



        
