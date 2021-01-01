>>> obj1 = Dog.objects.create(name='Max', data=None)  # SQL NULL.
<Dog: Max>
>>> obj2 = Dog.objects.create(name='Archie', data=Value('null'))  # JSON null.
<Dog: Archie>
>>> Dog.objects.filter(data=None)
<QuerySet [<Dog: Archie>]>
>>> Dog.objects.filter(data=Value('null'))
<QuerySet [<Dog: Archie>]>
>>> Dog.objects.filter(data__isnull=True)
<QuerySet [<Dog: Max>]>
>>> Dog.objects.filter(data__isnull=False)
<QuerySet [<Dog: Archie>]>
>>> obj1.data is None
True
>>> obj2.data is None
True
