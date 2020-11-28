# django.db.backends.sqlite3.base
class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'sqlite'
    display_name = 'SQLite'
    data_types = {
        ...
        'JSONField': 'text',
        ...
    }
    data_type_check_constraints = {
        ...
        'JSONField': '(JSON_VALID("%(column)s") OR "%(column)s" IS NULL)',
        ...
    }
