import subprocess
import json

KEY_TO_REPLACE = "COMMAND_HERE"


class Player():

    commands_json = None

    def __init__(self
                 ):

        with open('pipewire_python/pipewireAPICommands.json', 'r') as json_file:
            self.commands_json = json.load(json_file)

    def play_WAV_File(self,
                      audio_path
                      ):
        """
        Execute pipewire command to play a WAV file

        Args:
            - audio_path (str): path of the file to be played. Example: 'audios/my_audio.wav'
        Return:
            - shell_result (str): shell response to the command
        """

        command = self.commands_json['play']
        # Replace COMMAND_HERE to fill the command
        command_structure = [item.replace(
            KEY_TO_REPLACE, audio_path) for item in command]
        MyOut = subprocess.Popen(command_structure,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        stdout, stderr = MyOut.communicate()
        # print(stdout) empty b'' if correct
        # print(stderr) None if correct
        return stdout,stderr
