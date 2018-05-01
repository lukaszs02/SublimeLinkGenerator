import sublime
import sublime_plugin


class GeneratelinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("GenerateLink")
        print(self.view.window().project_file_name())

