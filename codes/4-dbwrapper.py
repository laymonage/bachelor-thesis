# django.db.backends.mysql.base
class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'mysql'
    data_types = {
        ...
        'JSONField': 'json',
        ...
    }
    ...

    @cached_property
    def data_type_check_constraints(self):
        if self.features.supports_column_check_constraints:
            check_constraints = {
                ...
            }
            if self.mysql_is_mariadb and self.mysql_version < (10, 4, 3):
                check_constraints['JSONField'] = 'JSON_VALID(`%(column)s`)'
            return check_constraints
        return {}


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


# django.db.backends.postgresql.base
class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'postgresql'
    display_name = 'PostgreSQL'
    data_types = {
        ...
        'JSONField': 'jsonb',
        ...
    }


# django.db.backends.sqlite.base
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
