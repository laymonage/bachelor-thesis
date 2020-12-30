class KeyTransform(BuiltinKeyTransform):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            'django.contrib.postgres.fields.jsonb.KeyTransform is deprecated '
            'in favor of django.db.models.fields.json.KeyTransform.',
            RemovedInDjango40Warning, stacklevel=2,
        )
        super().__init__(*args, **kwargs)


class KeyTextTransform(BuiltinKeyTextTransform):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            'django.contrib.postgres.fields.jsonb.KeyTextTransform is '
            'deprecated in favor of '
            'django.db.models.fields.json.KeyTextTransform.',
            RemovedInDjango40Warning, stacklevel=2,
        )
        super().__init__(*args, **kwargs)
