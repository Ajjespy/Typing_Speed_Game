"""THIS IS A WORK IN PROGRESS"""
# TODO fade music on transitions, SFX, etc.
from arcade import Sound
import string
import time

DEFAULT_MUSIC_VOLUME = 0.5
DEFAULT_SFX_VOLUME = 0.3
MAX_ALLOWED_VOLUME = 3


class SoundHandler(Sound):
    """Plays and modifies SFX and music"""

    def __init__(self) -> None:
        self.master_volume = 0
        self.setup()


    def setup(self) -> None:
        pass


    def set_master_volume(self, new_volume_mod) -> None:
        self.master_volume = new_volume_mod

    def _set_volume(self, volume, player) -> None:
        """Private: Do not call outside of class."""
        return super().set_volume(volume, player)

    def get_stream_position(self, player) -> float:
        """Returns position in the sound file in seconds. Resets to 0.0 when sound finishes."""
        return super().get_stream_position(player)


    def stop(self, player) -> None:
        """Stops current sound player"""
        return super().stop(player)

class MusicHandler(SoundHandler):

    def __init__(self, index=0) -> None:
        super().__init__()
        self.music_list = None
        self.sound = None
        self.current_player = None
        self.current_sound_index = index
        self.music_volume_modifier = DEFAULT_MUSIC_VOLUME
        self.music_volume = self.music_volume_modifier + self.master_volume
        self.fade_rate = 0.01

    def _update_music_volume(self) -> float:
        """Private: Do not call outside of class"""
        new_music_volume = self.music_volume_modifier + self.master_volume
        if new_music_volume > MAX_ALLOWED_VOLUME:
            self.music_volume = MAX_ALLOWED_VOLUME
        else:
            self.music_volume = new_music_volume
        return self.music_volume

    def set_music_volume(self, new_volume_mod:float) -> None:
        self.music_volume_modifier = new_volume_mod
        self._set_volume(self._update_music_volume(), self.current_player)
        

    def play_song(self, song:string, loop:bool=True) -> None:
        """ Parameters: 
                song (string): filepath to the song
                loop (bool): if true the music will loop """

        if self.sound:  # Stops overlapping music. Cleans any old players.
            self.stop(self.current_player)
            del self.current_player

        # Play the next song
        self.sound = Sound(song, streaming=True)
        self.current_player = self.sound.play(self.music_volume, loop=loop)
        
        time.sleep(0.03)  # Small delay so the function doesn't skip a track


class SFXHandler(SoundHandler):
    def __init__(self) -> None:
        super().__init__()
        self.sfx_list = None
        self.sound = None
        self.current_player = None
        self.current_sfx_index = 0
        self.sfx_volume_modifier = DEFAULT_SFX_VOLUME
        self.sfx_volume = self.sfx_volume_modifier + self.master_volume

    def update_sfx_volume(self) -> None:
        self.music_volume = self.music_volume_modifier + self.master_volume

    def set_sfx_volume(self, new_volume_mod) -> None:
        self.music_volume_modifier = new_volume_mod
        self.update_sfx_volume()


    def play_sfx(self, effect:string, loop:bool=False) -> None:
        """ Plays song. """

        if self.sound:  # Stops overlapping music. Cleans any old players.
            self.stop(self.current_player)
            del self.current_player

        # Play the next song
        self.sound = Sound(effect, streaming=True)
        self.current_player = self.sound.play(self.sfx_volume, loop=loop)
        # Small delay so the function doesn't skip a track
        time.sleep(0.03)
