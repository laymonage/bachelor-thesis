# django.db.backends.sqlite3.features
class DatabaseFeatures(BaseDatabaseFeatures):
    ...
    @cached_property
    def supports_json_field(self):
        try:
            with self.connection.cursor() as cursor, transaction.atomic():
                cursor.execute('SELECT JSON(\'{"a": "b"}\')')
        except OperationalError:
            return False
        return True
