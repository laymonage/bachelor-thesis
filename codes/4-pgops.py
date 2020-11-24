class DatabaseOperations(BaseDatabaseOperations):
    ...

    def json_cast_text_sql(self, field_name):
        return '(%s)::text' % field_name
