from kivy.uix.splitter import Splitter

class ScrollableLabelSplitter(Splitter):
    def __init__(self, **kwargs):
        Splitter.__init__(self, **kwargs)
        self.sizable_from = "bottom"
        self.min_size = 100
        self.max_size = 250
    @property
    def labelText(self):
        return self.ids.label.text if self.ids.label.text else ''

    @labelText.setter
    def labelText(self, value):
        self.ids.label.text = value
    
    @property
    def textContent(self):
        return self.ids.textContent.text

    @textContent.setter
    def textContent(self, value):
        self.ids.textContent.text = value
        
