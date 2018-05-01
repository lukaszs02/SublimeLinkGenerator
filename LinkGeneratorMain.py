import sublime
import sublime_plugin


class GeneratelinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings('LinkGenerator.sublime-settings')
        link = settings.get("url") + settings.get("lineSeparator") + str(self.current_line())
        print(link)


    def current_line(self):
        return (self.view.rowcol(self.view.sel()[0].begin())[0]) + 1