class HasKey(HasKeyLookup):
    lookup_name = 'has_key'
    postgres_operator = '?'
    prepare_rhs = False
