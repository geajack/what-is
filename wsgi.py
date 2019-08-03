from flask import Flask

from what_is import what_is, CantFindThing

app = Flask("What Is")

@app.errorhandler(CantFindThing)
def handle_cant_find(exception):
    return f"I don't know what \"{exception.thing}\" is.", 404

@app.route("/<thing>", methods=["GET"])
def query(thing):
    return what_is(thing)

if __name__ == "__main__":
    app.run()