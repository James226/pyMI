import os
import cherrypy

import Handlers
import UI.Web as ui

		
class WebServer:
    @cherrypy.expose
    def index(self, *args, **kwargs):
        index = Handlers.index.Index(ui.index.Index(args, kwargs))
        return index.Process()

settings = os.path.join(os.path.dirname(__file__), 'settings.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(WebServer(), config=settings)
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(WebServer(), config=settings)
