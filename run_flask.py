from api.core import create_app,cleanup_app

app = create_app()

if __name__ == '__main__':

    ip = '0.0.0.0'
    port = 5000
    debug_mode = True

    try:
        app.run(host=ip,port=port,debug=debug_mode)
    finally:
        cleanup_app()