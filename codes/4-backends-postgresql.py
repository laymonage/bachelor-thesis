# django.db.backends.postgresql.base
class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'postgresql'
    display_name = 'PostgreSQL'
    data_types = {
        ...
        'JSONField': 'jsonb',
        ...
    }

# django.db.backends.postgresql.features
class DatabaseFeatures(BaseDatabaseFeatures):
    ...
    has_native_json_field = True
