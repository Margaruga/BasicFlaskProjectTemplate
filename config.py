
# -*- coding: utf-8 -*-

class Config:
    DEBUG   = False
    TESTING = False
    SECRET_KEY = ''

class ProductionConfig(Config):
    pass
    
class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
