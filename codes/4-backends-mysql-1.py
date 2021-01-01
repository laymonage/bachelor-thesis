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
