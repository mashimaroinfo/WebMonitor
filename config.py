# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-02-15 19:35:17
# @Last Modified time: 2019-03-13 17:09:23
import os
import logging
import logging.config

basedir = os.path.abspath(os.path.dirname(__file__))

os.makedirs('log', exist_ok=True)
logging.config.fileConfig('log.conf')
logger = logging.getLogger()
logger.info('Finish loading config')


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = 'chinano.1'
    BABEL_DEFAULT_LOCALE = 'zh_CN'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
