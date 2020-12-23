def validate_cart_products_list(products):
    if not isinstance(products, list):
        raise ValidationError('Cart products should be a list.')
