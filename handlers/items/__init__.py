import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2

from model.item import Item


class ItemHandler(webapp2.RequestHandler):

    def get(self):
        items = Item.query(Item.owner == users.get_current_user().user_id()).order(-Item.added)

        jinja = jinja2.get_jinja2(app=self.app)
        valores = {"items": items}
        self.response.write(jinja.render_template('/items.html', **valores))


app = webapp2.WSGIApplication([
    ('/items', ItemHandler)
], debug=True)
