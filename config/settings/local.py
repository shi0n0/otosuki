from .base import *
import environ

root = environ.Path(__file__) - 3 # 
env_file = str(root.path('.env'))
env = environ.Env()
env.read_env(env_file) 

DEBUG = env('DEBUG')

DATABASES = {
    'default': env.db()
}