def prepare_value(self, value):
    if isinstance(value, InvalidJSONInput):
        return value
    return json.dumps(value, ensure_ascii=False, cls=self.encoder)

def has_changed(self, initial, data):
    if super().has_changed(initial, data):
        return True
    # For purposes of seeing whether something has changed, True isn't the
    # same as 1 and the order of keys doesn't matter.
    return (
        json.dumps(initial, sort_keys=True, cls=self.encoder) !=
        json.dumps(self.to_python(data), sort_keys=True, cls=self.encoder)
    )
