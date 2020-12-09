def field_cast_sql(self, db_type, internal_type):
    if db_type and db_type.endswith('LOB') and internal_type != 'JSONField':
        return "DBMS_LOB.SUBSTR(%s)"
    ...

def lookup_cast(self, lookup_type, internal_type=None):
    ...
    if internal_type == 'JSONField' and lookup_type == 'exact':
        return 'DBMS_LOB.SUBSTR(%s)'
    return "%s"
