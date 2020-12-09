class HasKeyLookup(PostgresOperatorLookup):
    logical_operator = None

    def as_sql(self, compiler, connection, template=None):
        # Process JSON path from the left-hand side.
        if isinstance(self.lhs, KeyTransform):
            lhs, lhs_params, lhs_key_transforms = self.lhs.preprocess_lhs(
                compiler, connection
            )
            lhs_json_path = compile_json_path(lhs_key_transforms)
        else:
            lhs, lhs_params = self.process_lhs(compiler, connection)
            lhs_json_path = '$'
        sql = template % lhs
        # Process JSON path from the right-hand side.
        rhs = self.rhs
        rhs_params = []
        if not isinstance(rhs, (list, tuple)):
            rhs = [rhs]
        for key in rhs:
            if isinstance(key, KeyTransform):
                *_, rhs_key_transforms = key.preprocess_lhs(
                    compiler, connection
                )
            else:
                rhs_key_transforms = [key]
            rhs_params.append('%s%s' % (
                lhs_json_path,
                compile_json_path(rhs_key_transforms, include_root=False),
            ))
        # Add condition for each key.
        if self.logical_operator:
            sql = (
                '(%s)' % self.logical_operator.join([sql] * len(rhs_params))
            )
        return sql, tuple(lhs_params) + tuple(rhs_params)
