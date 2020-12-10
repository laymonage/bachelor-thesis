class KeyTransformExact(JSONExact):
    def process_lhs(self, compiler, connection):
        lhs, lhs_params = super().process_lhs(compiler, connection)
        if connection.vendor == 'sqlite':
            rhs, rhs_params = super().process_rhs(compiler, connection)
            if rhs == '%s' and rhs_params == ['null']:
                lhs, _ = self.lhs.preprocess_lhs(
                    compiler, connection, lhs_only=True
                )
                lhs = 'JSON_TYPE(%s, %%s)' % lhs
        return lhs, lhs_params
