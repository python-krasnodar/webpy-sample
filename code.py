import web
import settings


db = web.database('postgres://' + settings.DB_USER + ':' + settings.DB_PASS
                  + '@' + settings.DB_HOST + ':' + settings.DB_PORT
                  + '/' + settings.DB_NAME)
render = web.template.render('templates/')
urls = (
    '/(.*)', 'index',
)

class index:
    def GET(self, name):
        return render.index(name)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
