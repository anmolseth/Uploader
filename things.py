import falcon

class Things:
	def on_get(self,req,resp):
		resp.body = ("\nI've always been more interested in\n")

app = falcon.API()
things = Things()
app.add_route('/things',things)