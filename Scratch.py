import sublime
import sublime_plugin
import re
import os

class ScratchCommand(sublime_plugin.WindowCommand):
    def run(self):
        save_path = self._getPath()
        save_extension = self._getExtension()

        #Ensure directory exists
        try:
            os.mkdir(self._getPath())
        except OSError:
            pass

        new_int = self._getNextInt(save_path)

        filename = save_path + "/" + str(new_int) + save_extension
        self.window.open_file(filename)

    def _getPath(self):
        s = sublime.load_settings("Scratch.sublime-settings")
        save_path = s.get("save_path", "~/Documents/Scratch")
        if save_path[0] == '~':
            save_path = os.path.expanduser('~') + save_path[1:]
        return save_path

    def _getExtension(self):
        s = sublime.load_settings("Scratch.sublime-settings")
        save_extension = s.get("extension", ".scratch")
        return save_extension

    def _getNextInt(self, directory):
        """Return the next highest integer to be used for a filename in directory"""
        files = os.listdir(directory)
        max = -1

        for file_name in files:
            m = re.match(r"(\d+).",file_name)
            if m and int(m.group(1)) > max:
                max = int(m.group(1))

        return max + 1
