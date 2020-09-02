#!/usr/bin/python3
"""comment"""
if __name__ == '__main__':
    from flask import Flask
    from flask import render_template
    from models import storage
    from operator import attrgetter
    app = Flask(__name__)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        """fetch"""
        state = storage.all("State")
        res = state.values()
        states_result = sorted(res, key=attrgetter('name'))
        return render_template('7-states_list.html',
                               states_result=states_result)

    @app.teardown_appcontext
    def teardown(self):
        """close"""
        storage.close()

    app.run(host='0.0.0.0', port='5000')
