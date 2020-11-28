# django.db.backends.oracle.operations
class DatabaseOperations(BaseDatabaseOperations):
    ...
    def get_db_converters(self, expression):
        converters = super().get_db_converters(expression)
        internal_type = expression.output_field.get_internal_type()
        if internal_type in ['JSONField', 'TextField']:
            converters.append(self.convert_textfield_value)
        ...
