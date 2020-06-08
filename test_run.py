from discogs_wrapper import DV


dv_instance = DV("FooBarApp/3.0")
response = dv_instance.delete_release_user(release_id='2095711',username = 'gbhase2',token='')
print(response)

