class DatabaseWrapper(BaseDatabaseWrapper):
    ...

    @async_unsafe
    def get_new_connection(self, conn_params):
        connection = Database.connect(**conn_params)
        ...
        psycopg2.extras.register_default_jsonb(
            conn_or_curs=connection, loads=lambda x: x
        )
        return connection
