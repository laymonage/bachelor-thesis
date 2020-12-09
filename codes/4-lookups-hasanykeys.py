class HasAnyKeys(HasKeys):
    lookup_name = 'has_any_keys'
    postgres_operator = '?|'
    logical_operator = ' OR '
