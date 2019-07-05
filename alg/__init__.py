"""
celery worker -A alg -l INFO
"""

from celery import Celery
celery=Celery("Lip")
celery.config_from_object("alg.celery_config")