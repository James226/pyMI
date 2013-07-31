class Index(object):
    def __init__(self, args, kwargs):
        self.value = ''
        self.args = args
        self.kwargs = kwargs
        self.Callbacks = {}

    def SetText(self, val):
        self.value = val

    def DisplayFiles(self, files):
        pass

    def Callback(self, name):
        if name in self.Callbacks:
            self.Callbacks[name]()

    def Render(self):
        if 'Submit' in self.kwargs:
            self.Callback('Submit')
        
        return self.value + '<form method="post" action=""><input type="submit" name="Submit" value="Submit" /></form>'