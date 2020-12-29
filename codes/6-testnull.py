@skipUnlessDBFeature('supports_json_field')
class TestSaveLoad(TestCase):
    @skipUnlessDBFeature('supports_primitives_in_json_field')
    def test_json_null_different_from_sql_null(self):
        json_null = NullableJSONModel.objects.create(value=Value('null'))
        json_null.refresh_from_db()
        sql_null = NullableJSONModel.objects.create(value=None)
        sql_null.refresh_from_db()
        # 'null' is not equal to NULL in the database.
        self.assertSequenceEqual(
            NullableJSONModel.objects.filter(value=Value('null')),
            [json_null],
        )
        self.assertSequenceEqual(
            NullableJSONModel.objects.filter(value=None),
            [json_null],
        )
        self.assertSequenceEqual(
            NullableJSONModel.objects.filter(value__isnull=True),
            [sql_null],
        )
        # 'null' is equal to NULL in Python (None).
        self.assertEqual(json_null.value, sql_null.value)
    ...
