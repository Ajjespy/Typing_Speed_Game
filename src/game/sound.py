"""THIS IS A WORK IN PROGRESS"""
# TODO fade music on transitions, SFX, etc.
from arcade import Sound
import time

DEFAULT_MUSIC_VOLUME = 0.5
DEFAULT_SFX_VOLUME = 0.5
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
        """Do not call outside of class."""
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
        self.fade_rate = self.music_volume * 0.1

    def update_music_volume(self) -> float:
        new_music_volume = self.music_volume_modifier + self.master_volume
        if new_music_volume > MAX_ALLOWED_VOLUME:
            self.music_volume = MAX_ALLOWED_VOLUME
        else:
            self.music_volume = new_music_volume
        return self.music_volume

    def set_music_volume(self, new_volume_mod: float) -> None:
        self.music_volume_modifier = new_volume_mod
        self._set_volume(self.update_music_volume(), self.current_player)
        

    def update_music_list(self, music_list) -> None:
        """ Updates music list.
            Parameters: 
                music_list (list): list of file paths to sound files"""
        self.music_list = music_list

    def advance_song(self) -> None:
        """Advance our pointer to the next song in self.music_list. Not used when music loops."""
        self.current_sound_index += 1
        if self.current_sound_index >= len(self._list):
            self.current_sound_index = 0


    def play_song(self, loop=True) -> None:
        """ Plays song. """

        if not len(self.music_list):  # Stops player if self.music_list is empty
            self.stop(self.current_player)
            return

        if self.sound:  # Stops overlapping music. Cleans any old players.
            self.stop(self.current_player)
            del self.current_player

        # Play the next song
        self.sound = Sound(self.music_list[self.current_sound_index], streaming=True)
        self.current_player = self.sound.play(self.music_volume, loop=loop)
        # Small delay so the function doesn't skip a track
        time.sleep(0.03)


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


    def update_sfx_list(self, sfx_list) -> None:
        """ Updates sfx list.
            Parameters: 
                sfx_list (list): list of file paths to sound files"""
        self.sfx_list = sfx_list

    def select_sfx(self, index):
        """Select sfx by index in sfx_list"""
        if index not in self.sfx_list:
            raise ValueError
        self.current_sfx_index = index


    def play_sfx(self, loop=False) -> None:
        """ Plays song. """

        if not len(self.sfx_list):  # Stops player if self.music_list is empty
            self.stop(self.current_player)
            return

        if self.sound:  # Stops overlapping music. Cleans any old players.
            self.stop(self.current_player)
            del self.current_player

        # Play the next song
        self.sound = Sound(self.sfx_list[self.current_sfx_index], streaming=True)
        self.current_player = self.sound.play(self.sfx_volume, loop=loop)
        # Small delay so the function doesn't skip a track
        time.sleep(0.03)
