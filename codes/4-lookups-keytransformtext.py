class KeyTransformIExact(
    CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IExact):
    pass


class KeyTransformIContains(
    CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IContains):
    pass


class KeyTransformStartsWith(
    KeyTransformTextLookupMixin, lookups.StartsWith):
    pass


class KeyTransformIStartsWith(
    CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IStartsWith):
    pass


class KeyTransformEndsWith(
    KeyTransformTextLookupMixin, lookups.EndsWith):
    pass


class KeyTransformIEndsWith(
    CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IEndsWith):
    pass


class KeyTransformRegex(
    KeyTransformTextLookupMixin, lookups.Regex):
    pass


class KeyTransformIRegex(
    CaseInsensitiveMixin, KeyTransformTextLookupMixin, lookups.IRegex):
    pass
