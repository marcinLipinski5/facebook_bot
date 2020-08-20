from fb_api import app

if __name__ == '__main__':
    app.run(port=444, host='0.0.0.0', threaded=True, debug=True)

