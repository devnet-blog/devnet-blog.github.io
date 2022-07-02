# CHANELOG

List of changes for site deployment process. 

## 0.2.3 - 04.04.2022

- Restore previous header logo image.

## 0.1.3 - 04.04.2022

- Modified information about authors
- Add Article set_logger

## 0.1.2 - 21.03.2022

### Changed

- Updated `README.md` with more valid and useful content.

### Remove

- From `tasks.py` removed all unnecessary, not used or not required tasks.

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