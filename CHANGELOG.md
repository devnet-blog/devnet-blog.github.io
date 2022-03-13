# CHANELOG

List of changes for site deployment process. 

## 0.1.1 - 13.03.2022

### Remove

- Remove file `CNAME` from root directory. Not required here. 

### Change

- Update `requirements.txt`


## 0.1.0 - 13.03.2022

### Change

- Header image for more blurish one. 
  - Old header renamed from `main_header.jpg` -> `old_main_header.jpg`
  - Adjust `pelicanconf.py` accordingly. 
- In template `base.html`:
  - Replace `<a class="navbar-brand" href="{{ SITEURL }}/">{{ SITENAME }}</a>` with _INDEX_ text: `<a class="navbar-brand" href="{{ SITEURL }}/">INDEX</a>` 