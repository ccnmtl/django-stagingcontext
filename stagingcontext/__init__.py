from django.conf import settings
import os.path
import time


def staging_processor(request):
    return {
        'STAGING_ENV': getattr(settings, 'STAGING_ENV', False),
        # since our deploy process wipes and recreates the virtualenv
        # each time, we can rely on the modification time for this file
        # roughly reflecting the deployment time
        # the 'apache/django.wsgi' file for a project would be more accurate
        'STAGING_DEPLOY_TIME': time.ctime(os.path.getmtime(__file__))
    }
