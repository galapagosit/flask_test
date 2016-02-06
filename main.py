from flask import Flask, current_app
import flask

app_1 = Flask('1')
app_2 = Flask('2')


if __name__ == "__main__":
    with app_1.app_context():
        print(current_app)
        with app_2.app_context():
            print(current_app)
            import pprint
            pprint.pprint(flask._app_ctx_stack)
        print(current_app)

