# django.db.backends.oracle.base
class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'oracle'
    display_name = 'Oracle'
    data_types = {
        ...
        'JSONField': 'NCLOB',
        ...
    }
    data_type_check_constraints = {
        ...
        'JSONField': '%(qn_column)s IS JSON',
        ...
    }
