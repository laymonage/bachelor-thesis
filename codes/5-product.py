class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock_qty = models.PositiveIntegerField()
    data = models.JSONField(default=dict, blank=True)
