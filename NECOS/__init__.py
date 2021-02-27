# coding=UTF-8

#플라스크 불러오기
from flask import Flask
#플라스크 마이그레이션 불러오기
from flask_migrate import Migrate
#플라스크 SQLALCHEMY 불러오기
from flask_sqlalchemy import SQLAlchemy

#직접 만든 'config.py' 불러오기
import config

#데이터베이스 객체
db = SQLAlchemy()
#마이그레이션 객체
migrate = Migrate()


def create_app():
    app=Flask(__name__)
    app.config.from_object(config)
    
    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    
    #Blueprint
    from .views import main_views
    app.register_blueprint(main_views.blueprint)
        
    return app
    