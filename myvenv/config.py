#i removed password
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:INSERT_PASSWORD@localhost/mechanic_mod'
    DEBUG = True
    CACHE_TYPE = "SimpleCache"


class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    CACHE_TYPE = "NullCache"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Bebop1216!@localhost/mechanic_mod_prod'
    CACHE_TYPE = "SimpleCache"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
