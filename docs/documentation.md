
## Instantiate the wrapper
```bash
from discogs_wrapper import DV

dv_instance = DV("FooBarApp/3.0")
```

## Release Resource

Fetch a release 
```bash
dv_instance.get_release(id='123',curr_abbr='123')
```
Delete a release 
```bash
dv_instance.delete_release_user(release_id='123',username='memory',token='abc123')
```

## Release Rating by User
```bash
dv_instance.get_release_rating_by_user(release_id='123',username='memory')
```
## Community Rating 
```bash
dv_instance.get_community_release_rating(release_id='123')
```
## Masters Release
```bash
dv_instance.get_masters_release(master_id='123')
```
## Masters Release Versions
```bash
dv_instance.get_masters_release_version(master_id='123',page='',per_page='')
```
## Artist
```bash
dv_instance.get_artist(artist_id='123')
```
        
## Artist Releases
```bash
dv_instance.get_artist_releases(artist_id='123',sort='',sort_order='')
```

## Label
```bash
dv_instance.get_label(label_id='123')
```

## All Label Releases
```bash
dv_instance.get_all_label_releases(label_id='123',page='',per_page='')
```

## Search
```bash
dv_instance.get_search(q='abcd',token='abcd123',title='',typee='',release_title='',credit='',artist='',anv='',label='',genre='',style='',country='',year='',formatt = '',catno='',barcode='',track='',submitter='',contributor='',key='',secret='')
```
