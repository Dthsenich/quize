from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy

# импорт всех функций из файлов для базы данных

from databace.leaderservice import *
from databace.questionservice import *
from databace.registerservice import *
