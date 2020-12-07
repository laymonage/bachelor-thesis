def as_oracle(self, compiler, connection):
    lhs, params, key_transforms = self.preprocess_lhs(compiler, connection)
    json_path = compile_json_path(key_transforms)
    return (
        "COALESCE(JSON_QUERY(%s, '%s'), JSON_VALUE(%s, '%s'))" %
        ((lhs, json_path) * 2)
    ), tuple(params) * 2
