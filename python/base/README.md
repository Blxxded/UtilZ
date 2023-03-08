# 🩸 | Usage of utilz_base.py

<p>Import the BASE class:</p>

```python
from utilz_base import BASE
```

<p>And now you can easily decode and encode to ASCII85, BASE16, BASE32, BASE64 and SAFE URL BASE64:</p>

```python
BASE.Decode.A85("E&;WWG;+&J", "ascii")
BASE.Encode.B16("p4ssw0rd", "ascii")
BASE.Decode.B32("OA2HG43XGBZGI===", "utf-8")
BASE.Encode.B64("p4ssw0rd", "utf-8")
BASE.Decode.URL_B64("彟眵䑁䅑督穂䡁䅣䅍祂䝁䅑", "utf-16")
```
<p><b>(CHARSET IS OPTIONAL)</b> When there's no charset argumented, "utf-8" is set by default:</p>

```python
BASE.Decode.A85("E&;WWG;+&J")
BASE.Encode.B16("p4ssw0rd")
BASE.Decode.B32("OA2HG43XGBZGI===")
BASE.Encode.B64("p4ssw0rd")
BASE.Decode.URL_B64("cDRzc3cwcmQ=")
```
