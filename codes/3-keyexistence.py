>>> Dog.objects.filter(data__has_key='breed')
<QuerySet [<Dog: Rufus>, <Dog: Meg>, <Dog: Cooper>]>
>>> Dog.objects.filter(data__has_keys=['breed', 'owner'])
<QuerySet [<Dog: Rufus>, <Dog: Meg>]>
>>> Dog.objects.filter(data__has_any_keys=['breed', 'age'])
<QuerySet [<Dog: Rufus>, <Dog: Meg>, <Dog: Cooper>]>
