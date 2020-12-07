def as_sql(self, compiler, connection):
    ...
    try:
        int(self.key_name)
    except ValueError:
        lookup = "'%s'" % self.key_name
    else:
        lookup = "%s" % self.key_name
    return "(%s %s %s)" % (lhs, self.operator, lookup), params
