class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.JSONField(
        default=list,
        blank=True,
        validators=[
            validate_cart_products_list,
                validate_cart_product_ids_exist,
        ],
    )
