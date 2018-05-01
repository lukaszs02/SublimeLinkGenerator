from os.path import dirname, realpath
import os
import re
import sublime
import sublime_plugin

class GeneratelinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings('LinkGenerator.sublime-settings')
        link = settings.get("url") + self.file_path() + settings.get("lineNumberSeparator") + str(self.current_line())
        print(link)
        self.copy_link_to_clipboard(link)

    def current_line(self):
        return (self.view.rowcol(self.view.sel()[0].begin())[0]) + 1

    def file_path(self):
        project_folder = re.search("[^/]*$", str(self.view.window().extract_variables()['folder'])).group(0)
        file_patch = re.search(project_folder + "/.*[^/]*$", str(self.view.window().extract_variables()['file'])).group(0)
        return file_patch

    def copy_link_to_clipboard(self, txt):
        os.system("echo '%s' | pbcopy" % txt)
