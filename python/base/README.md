# 🩸 | Usage of utilz_base.py

<p>Import the BASE class:</p>

```python
from utilz_base import BASE
```

<p>And now you can easily decode and encode to ASCII85, BASE16, BASE32, BASE64 and SAFE URL BASE64:</p>

```python
BASE.A85("p4ssw0rd", "ascii")
BASE.B16("p4ssw0rd", "cp1252")
BASE.B32("p4ssw0rd", "utf-8")
BASE.B64("p4ssw0rd", "utf-16")
BASE.URL_B64("p4ssw0rd", "utf-32")
```
<p><b>(CHARSET IS OPTIONAL)</b> When there's no charset argumented, "utf-8" is set by default:</p>

```python
BASE.A85("p4ssw0rd")
BASE.B16("p4ssw0rd")
BASE.B32("p4ssw0rd")
BASE.B64("p4ssw0rd")
BASE.URL_B64("p4ssw0rd")
```
