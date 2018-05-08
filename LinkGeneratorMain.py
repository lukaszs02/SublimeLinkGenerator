from os.path import dirname, realpath
import os
import re
import sublime
import sublime_plugin
 
class GeneratelinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        link = self.generateLink()
        print(link)
        sublime.set_clipboard(link)
 
    def generateLink(self):
        settings = sublime.load_settings('LinkGenerator.sublime-settings')
        if(re.search("gitlab|github", settings.get("url"))):
            link = settings.get("url") + self.projectName() + "/blob/" + self.getBranch(settings) + self.filePath() + settings.get("lineNumberSeparator") + str(self.currentLine())
        else:
            link = settings.get("url") + self.projectName() + self.filePath() + settings.get("lineNumberSeparator") + str(self.currentLine())
        return link
 
    def currentLine(self):
        return (self.view.rowcol(self.view.sel()[0].begin())[0]) + 1
 
    def projectName(self):
         projectName = re.search(r'[^(\\|/)]*$', str(self.view.window().extract_variables()['folder'])).group(0)
         return projectName
 
    def filePath(self):
        project_folder = self.projectName()
        file_patch = re.search(r'(?:' + project_folder + r')(.*$)', str(self.view.window().extract_variables()['file'])).group(1)
        return file_patch
 
    def getBranch(self, settings):
        branch = settings.get("branch", "master")
        if(branch == "_auto"):
            branch = "master" #TODO add geting current branch form repository
        return branch
