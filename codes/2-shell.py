>>> config = {'dark_mode': True, 'font_size': 2, 'color_scheme': 'pink'}
>>> profile = Profile.objects.create(config=config)
>>> # Some time later...
>>> saved_profile = Profile.objects.get(id=profile.id)
>>> saved_profile.config == config
True
>>> saved_profile.config
{'dark_mode': True, 'font_size': 2, 'color_scheme': 'pink'}
>>> saved_profile.config['font_size'] = 3
>>> saved_profile.save()
>>> Profile.objects.get(id=saved_profile.id).config['font_size']
3
