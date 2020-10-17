>>> user1 = User.objects.get(id=1)
>>> config1 = {'dark_mode': True, 'font_size': 2, 'color_scheme': 'blue'}
>>> profile1 = Profile.objects.create(user=user1, config=config1)
>>> # Some time later...
>>> saved_profile = Profile.objects.get(user=user1)
>>> saved_profile.config == config1
True
>>> saved_profile.config
{'dark_mode': True, 'font_size': 2, 'color_scheme': 'blue'}
>>> saved_profile.config['font_size'] = 3
>>> saved_profile.save()
>>> Profile.objects.get(user=user1).config['font_size']
3
