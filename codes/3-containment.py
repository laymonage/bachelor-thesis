>>> Dog.objects.create(name='Max', data={'breed': 'beagle', 'owner': 'Bob'})
<Dog: Max>
>>> Dog.objects.create(name='Meg', data={'breed': 'collie', 'owner': 'Bob'})
<Dog: Meg>
>>> Dog.objects.create(name='Fred', data={})
<Dog: Fred>
>>> Dog.objects.filter(data__contains={'owner': 'Bob'})
<QuerySet [<Dog: Max>, <Dog: Meg>]>
>>> Dog.objects.filter(data__contains={'breed': 'collie'})
<QuerySet [<Dog: Meg>]>
>>> Dog.objects.filter(data__contained_by={'breed': 'collie', 'owner': 'Bob'})
<QuerySet [<Dog: Meg>, <Dog: Fred>]>
>>> Dog.objects.filter(data__contained_by={'breed': 'collie'})
<QuerySet [<Dog: Fred>]>
