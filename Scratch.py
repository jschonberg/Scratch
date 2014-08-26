import sublime
import sublime_plugin
import re
import os

def getPath():
        s = sublime.load_settings("Scratch.sublime-settings")
        save_path = s.get("save_path", "~/Documents/Scratch")
        if save_path[0] == '~':
            save_path = os.path.expanduser('~') + save_path[1:]
        return save_path

def getExtension():
    s = sublime.load_settings("Scratch.sublime-settings")
    save_extension = s.get("extension", ".scratch")
    return save_extension

class SyntaxPreSaveCommand(sublime_plugin.EventListener):
    def on_post_save(self, view):
        if not view.file_name().startswith(getPath()):
            return

        # If first line is a file extension:
        infile_re = re.match(r"\.\w+$",view.substr(view.line(0)))
        filename_re = re.match(r"(.+)(\.\w+)$",view.file_name())

        if infile_re and filename_re and infile_re.group() != filename_re.group(2):
            new_name = filename_re.group(1) + infile_re.group()
            os.rename(view.file_name(), new_name)
            with open(new_name, 'r') as fin:
                data = fin.read().splitlines(True)
            with open(new_name, 'w') as fout:
                fout.writelines(data[1:])
            sublime.active_window().run_command("close")
            sublime.active_window().open_file(new_name)

class ScratchCommand(sublime_plugin.WindowCommand):
    def run(self):
        save_path = getPath()
        save_extension = getExtension()

        #Ensure directory exists
        try:
            os.mkdir(getPath())
        except OSError:
            pass

        new_int = self._getNextInt(save_path)

        filename = save_path + "/" + str(new_int) + save_extension
        self.window.open_file(filename)

    def _getNextInt(self, directory):
        """Return the next highest integer to be used for a filename in directory"""
        files = os.listdir(directory)
        max = -1

        for file_name in files:
            m = re.match(r"(\d+).",file_name)
            if m and int(m.group(1)) > max:
                max = int(m.group(1))

        return max + 1
