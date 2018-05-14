# SublimeLinkGenerator
Sublime Text 3 plugin to generate link 
to your project web server repository base on the current file line.

![](https://thumbs.gfycat.com/AdmirableDearestHyena-size_restricted.gif)

## Installation

#### Windows
Download zip package and unzip it to your Sublime Text package directory:

```
%appdata%\Sublime Text 3\Packages
```

#### Linux/OSX
Manualy clone git repository [SublimeLinkGenerator](https://github.com/lukaszs02/SublimeLinkGenerator) to your package directory.

OSX
```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
$ git clone https://github.com/lukaszs02/SublimeLinkGenerator.git 
```

Linux
```
$ cd ~/.config/sublime-text-3/Packages/
$ git clone https://github.com/lukaszs02/SublimeLinkGenerator.git
```

## Before first use
Before first use you need edit file [LinkGeneration.sublime-settings](https://github.com/lukaszs02/SublimeLinkGenerator/blob/master/LinkGenerator.sublime-settings) and put then your remote repistory url, line number separator and git branch.