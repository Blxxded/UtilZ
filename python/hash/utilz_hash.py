# -*- coding: utf-8 -*-

import hashlib

class HASH():
	def MD5(Data : str, Charset : str = None):
		if Charset == None: hashlib.md5(Data.encode("utf-8")).digest().hex()
		else: hashlib.md5(Data.encode(Charset)).digest().hex()
	def SHA1(Data, Charset : str = None):
		if Charset == None: hashlib.sha1(Data.encode("utf-8")).digest().hex()
		else: hashlib.sha1(Data.encode(Charset)).digest().hex()
	def SHA224(Data, Charset : str = None):
		if Charset == None: hashlib.sha224(Data.encode("utf-8")).digest().hex()
		else: hashlib.sha224(Data.encode(Charset)).digest().hex()
	def SHA256(Data, Charset : str = None):
		if Charset == None: hashlib.sha256(Data.encode("utf-8")).digest().hex()
		else: hashlib.sha256(Data.encode(Charset)).digest().hex()
	def SHA384(Data, Charset : str = None):
		if Charset == None: hashlib.sha384(Data.encode("utf-8")).digest().hex()
		else: hashlib.sha384(Data.encode(Charset)).digest().hex()
	def SHA512(Data, Charset : str = None):
		if Charset == None: hashlib.sha512(Data.encode("utf-8")).digest().hex()
		else: hashlib.sha512(Data.encode(Charset)).digest().hex()
