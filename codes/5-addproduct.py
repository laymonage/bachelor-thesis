def add_product(self, product):
    for existing in self.products:
        if existing['id'] == product.id.hex:
            existing['quantity'] += 1
            break
    else:
        product_data = {
            'id': product.id.hex,
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        }
        self.products.append(product_data)
