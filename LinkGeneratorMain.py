import sublime
import sublime_plugin


class GeneratelinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")