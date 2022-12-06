from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from sweater.config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

# === ЕСЛИ В ИМПОРТ ДОБАВИТЬ utils.py ФАЙЛ ЧИТАЕТСЯ НО В БД НИЧЕГО НЕ ЗАГРУЖАЕТСЯ
# from sweater import models, views, utils
from sweater import models, views # ЕСЛИ ТАК ОСТАВИТЬ ТО ВСЕ РАБОТАЕТ

with app.app_context(): # ПОНЯТЬ КАК РАБОТАТЬ С ЭТИМ?
    # db.drop_all()
    db.create_all()


# with app.app_context():
#     try:
#         db.session.execute('DROP MATERIALIZED VIEW IF EXISTS search_view;')
#         db.session.commit()
#     except:
#         pass
#     db.session.remove()  # DO NOT DELETE THIS LINE. We need to close sessions before dropping tables.
#     db.drop_all()
