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

# django.db.backends.oracle.operations
class DatabaseOperations(BaseDatabaseOperations):
    ...
    def get_db_converters(self, expression):
        converters = super().get_db_converters(expression)
        internal_type = expression.output_field.get_internal_type()
        if internal_type in ['JSONField', 'TextField']:
            converters.append(self.convert_textfield_value)
        ...
