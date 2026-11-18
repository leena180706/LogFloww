
import atexit

from app import app, start_background_services, stop_background_services

start_background_services()

atexit.register(stop_background_services)
