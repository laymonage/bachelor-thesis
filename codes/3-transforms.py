>>> Dog.objects.filter(data__breed='collie')
<QuerySet [<Dog: Meg>]>
>>> Dog.objects.filter(data__owner__name='Bob')
<QuerySet [<Dog: Rufus>, <Dog: Meg>]>
>>> Dog.objects.filter(data__favorite_toys__0__type='plush')
<QuerySet [<Dog: Cooper>]>
>>> Dog.objects.filter(data__owner=None)
<QuerySet [<Dog: Cooper>]>
>>> Dog.objects.filter(data__owner__isnull=True)
<QuerySet [<Dog: Fred>]>
>>> Dog.objects.filter(data__breed__startswith='col')
<QuerySet [<Dog: Meg>]>
>>> Dog.objects.filter(data__favorite_toys__contains={'type': 'ball'})
<QuerySet [<Dog: Cooper>]>
>>> Dog.objects.filter(data__favorite_toys__1__has_key='color')
<QuerySet [<Dog: Cooper>]>
