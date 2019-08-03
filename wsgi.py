from flask import Flask

from what_is import what_is

app = Flask("What Is")

@app.route("/<thing>", methods=["GET"])
def query(thing):
    return what_is(thing)

if __name__ == "__main__":
    app.run()