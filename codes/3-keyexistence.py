>>> Dog.objects.filter(data__has_key='breed')
<QuerySet [<Dog: Rufus>, <Dog: Meg>, <Dog: Cooper>]>
>>> Dog.objects.filter(data__has_keys=['breed', 'favorite_toys'])
<QuerySet [<Dog: Cooper>]>
>>> Dog.objects.filter(data__has_any_keys=['breed', 'age', 'favorite_toys'])
<QuerySet [<Dog: Rufus>, <Dog: Meg>, <Dog: Cooper>]>
