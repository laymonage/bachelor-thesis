>>> Dog.objects.create(name='Rufus', data={'breed': 'beagle', 'owner': 'Bob'})
<Dog: Rufus>
>>> Dog.objects.create(name='Meg', data={'breed': 'collie', 'owner': 'Bob'})
<Dog: Meg>
>>> Dog.objects.create(name='Cooper', data={
...     'breed': 'labrador',
...     'owner': None,
...     'favorite_toys': [
...         {'type': 'plush', 'color': 'yellow'},
...         {'type': 'ball', 'color': 'white'},
...     ],
... })
<Dog: Cooper>
>>> Dog.objects.create(name='Fred', data={})
<Dog: Fred>
