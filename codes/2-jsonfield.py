import json
from psycopg2.extras import Json
...

class JsonAdapter(Json):
    """
    Customized psycopg2.extras.Json to allow for a custom encoder.
    """
    def __init__(self, adapted, dumps=None, encoder=None):
        self.encoder = encoder
        super().__init__(adapted, dumps=dumps)

    def dumps(self, obj):
        options = {'cls': self.encoder} if self.encoder else {}
        return json.dumps(obj, **options)

class JSONField(CheckFieldDefaultMixin, Field):
    ...
    def db_type(self, connection):
        return 'jsonb'

    def get_prep_value(self, value):
        if value is not None:
            return JsonAdapter(value, encoder=self.encoder)
        return value
