# -*- coding: utf-8 -*-

import base64

class BASE():
	class Decode():
		def A85(Data : str, Charset : str = None):
			if Charset == None: return base64.a85decode(Data.encode("utf-8")).decode("utf-8")
			else: return base64.a85decode(Data.encode(Charset)).decode(Charset)
		def B16(Data : str, Charset : str = None):
			if Charset == None: return base64.b16decode(Data.encode("utf-8")).decode("utf-8")
			else: return base64.b16decode(Data.encode(Charset)).decode(Charset)
		def B32(Data : str, Charset : str = None):
			if Charset == None: return base64.b32decode(Data.encode("utf-8")).decode("utf-8")
			else: return base64.b32decode(Data.encode(Charset)).decode(Charset)
		def B64(Data : str, Charset : str = None):
			if Charset == None: return base64.b64decode(Data.encode("utf-8")).decode("utf-8")
			else: return base64.b64decode(Data.encode(Charset)).decode(Charset)
		def URL_B64(Data : str, Charset : str = None):
			if Charset == None: return base64.urlsafe_b64decode(Data.encode("utf-8")).decode("utf-8")
			else: return base64.urlsafe_b64decode(Data.encode(Charset)).decode(Charset)
	class Encode():
		def A85(Data : str, Charset : str = None):
			if Charset == None: return base64.a85encode(Data.encode("utf-8")).decode("utf-8")
			else: return base64.a85encode(Data.encode(Charset)).decode(Charset)
		def B16(Data : str, Charset : str = None):
			if Charset == None: return base64.b16encode(Data.encode("utf-8")).decode("utf-8")
			else: return base64.b16encode(Data.encode(Charset)).decode(Charset)
		def B32(Data : str, Charset : str = None):
			if Charset == None: return base64.b32encode(Data.encode("utf-8")).decode("utf-8")
			else: return base64.b32encode(Data.encode(Charset)).decode(Charset)
		def B64(Data : str, Charset : str = None):
			if Charset == None: return base64.b64encode(Data.encode("utf-8")).decode("utf-8")
			else: return base64.b64encode(Data.encode(Charset)).decode(Charset)
		def URL_B64(Data : str, Charset : str = None):
			if Charset == None: return base64.urlsafe_b64encode(Data.encode("utf-8")).decode("utf-8")
			else: return base64.urlsafe_b64encode(Data.encode(Charset)).decode(Charset)
