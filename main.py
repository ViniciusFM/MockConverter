import kivy
from kivy.config import Config
Config.set('graphics','resizable',0)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import kivy.core.window
from plyer import filechooser
from kivy.factory import Factory

import os
import scroll_label
import color_res, string_res
from mock_parser import PatternTextConverter

WINDOWSIZE = 800, 600
ERR_COLOR = color_res.get_syntax_err_string_color_hex()
CANVACOLOR = color_res.get_main_canvas()

VERSION = "2.0a"
PROGRAM_NAME = "MockConverter "+VERSION

class RootLayoutController(BoxLayout):
    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.patternText = None

    # events
    def onClickChooseFile(self):
        choosenFile = filechooser.open_file(title=string_res.get(string_res.PICKJSON), 
                             filters=[("JavaScript Object Notation (.json)", "*.json")])
        if choosenFile:
            self.patternText = PatternTextConverter(choosenFile[0])
            self.ids.jsonPreview.textContent = self.patternText.getModelAsString()
            self.ids.patternText.disabled = False

    def saveConvertion(self, path):
        if self.patternText:
            converted = self.patternText.getConvertedData()
            with open(path, "w") as f:
                f.write(converted)

    def onClickConvert(self):
        if self.patternText and self.patternText.isPossibleToConvert():
            outputChoosenFile = filechooser.save_file(title=string_res.get(string_res.SAVEOUT),
                                            filters=[("Text (.txt)", "*.txt")])
            if outputChoosenFile:
                self.saveConvertion(outputChoosenFile[0])
        
    def onPatternInputChange(self, value):
        if self.patternText:
            if not value: 
                self.ids.conversionPreview.textContent = ''
                return
            parsedText = self.patternText.getParsePreview(value)
            if parsedText:
                self.ids.conversionPreview.textContent = parsedText
            else:
                last_text = self.ids.conversionPreview.textContent
                self.ids.conversionPreview.textContent = "[color="+ERR_COLOR+"]"+last_text+"[/color]"

class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

    def build(self):
        self.title = PROGRAM_NAME

if __name__ == "__main__":
    kivy.core.window.Window.size = WINDOWSIZE
    kivy.core.window.Window.clearcolor = CANVACOLOR
    MainApp().run()