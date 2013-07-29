

class Index(object):

    def __init__(self, ui):
        self.ui = ui
        self.ui.Callbacks['Submit'] = self.Submit

    def Process(self):
        self.ui.SetText('This is a test')
        return self.ui.Render()
        
    def Submit(self):
        self.ui.SetText('Submitted!')