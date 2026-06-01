import falcon
from wsgiref.simple_server import make_server
import json
from countryabs import national

class national_status():
    def on_get(self, req, resp):
        resp.text = json.dumps({"status":"success", "message":"ready to check country and provide information."})
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        try:
            user = national(req.media["name"],int(req.media["age"]),req.media["country"])
            resp.text = json.dumps({"status":"success", "message":user.get_statement()})
            resp.status = falcon.HTTP_200
        except Exception as err:
            resp.text = json.dumps({"status":"failure", "message":err})
            resp.status = falcon.HTTP_200

status_app = falcon.App()
national_status_app = national_status()
status_app.add_route("/status",national_status_app)

with make_server("",5000,status_app) as server:
    print(f'Running at {server.server_name} at {server.server_port}')
    server.serve_forever()