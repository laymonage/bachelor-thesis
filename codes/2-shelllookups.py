>>> user2 = User.objects.get(id=2)
>>> config2 = {
        'dark_mode': False,
        'color_scheme': 'red',
        'profile': {'show_birthday': False, 'is_private': True},
    }
>>> profile2 = Profile.objects.create(user=user2, config=config2)
>>> Profile.objects.filter(
...     config__contains={'profile': {'is_private': True})
<QuerySet [<Profile object (2)>]>
>>> Profile.objects.filter(config__has_key='color_scheme')
<QuerySet [<Profile object (1)>, <Profile object (2)>]>
>>> Profile.objects.filter(config__dark_mode=True)
<QuerySet [<Profile object (1)>]>
>>> Profile.objects.filter(config__profile__show_birthday=False)
<QuerySet [<Profile object (2)>]>
