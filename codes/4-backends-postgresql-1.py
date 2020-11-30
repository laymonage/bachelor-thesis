# django.db.backends.postgresql.base
class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'postgresql'
    display_name = 'PostgreSQL'
    data_types = {
        ...
        'JSONField': 'jsonb',
        ...
    }
