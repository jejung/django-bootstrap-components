from django.conf import settings as user_settings

class Settings(object):
    """ django.conf.settings wrapper to enable default settings to this app.
    """
    BOOTSTRAP = getattr(user_settings, 'BOOTSTRAP', {
        'FROM': 'static',
    })
    
    def __getattr__(self, name):
        if hasattr(Settings, name):
            return getattr(Settings, name)
        return getattr(user_settings, name)

settings = Settings()
