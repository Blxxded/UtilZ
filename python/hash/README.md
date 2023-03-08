# 🩸 | Usage of hash.py

<p>Import the HASH class:</p>

```python
from utilz_hash import HASH
```

<p>And now you can easily hash to MD5, SHA1, SHA224, SHA256, SHA384 and SHA512:</p>

```python
HASH.MD5("p4ssw0rd", "ascii")
HASH.SHA1("p4ssw0rd", "cp1252")
HASH.SHA224("p4ssw0rd", "utf-8")
HASH.SHA256("p4ssw0rd", "utf-16")
HASH.SHA384("p4ssw0rd", "utf-32")
HASH.SHA512("p4ssw0rd", "iso-8859-1")
```
<p><b>(CHARSET IS OPTIONAL)</b> When there's no charset argumented, "utf-8" is set by default:</p>

```python
HASH.MD5("p4ssw0rd")
HASH.SHA1("p4ssw0rd")
HASH.SHA224("p4ssw0rd")
HASH.SHA256("p4ssw0rd")
HASH.SHA384("p4ssw0rd")
HASH.SHA512("p4ssw0rd")
```
