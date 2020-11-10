>>> Dog.objects.filter(data__contains={'owner': 'Bob'})
<QuerySet [<Dog: Rufus>, <Dog: Meg>]>
>>> Dog.objects.filter(data__contains={'favorite_toys': [{'type': 'plush'}]})
<QuerySet [<Dog: Cooper>]>
>>> Dog.objects.filter(
        data__contained_by={'breed': 'collie', 'owner': 'Bob', 'age': 7})
<QuerySet [<Dog: Meg>, <Dog: Fred>]>
>>> Dog.objects.filter(data__contained_by={'breed': 'collie'})
<QuerySet [<Dog: Fred>]>
