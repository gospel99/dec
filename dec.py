try:
	import os,sys, platform, uncompyle6
except ImportError:
	os.system("pip2 install uncompyle6");os.system("python2 {}".format(sys.argv[0]))
merah, hijau, cyan, putih, ungu="\x1b[1;31m", "\x1b[1;32m","\x1b[1;36m","\x1b[1;37m","\x1b[1;35m"
def echo(satu):
	print(satu)
def keluar(dua):
	exit(dua)
class decompy:
	def __init__(self, file):
		self.buka=open(file,"r").read()
		self.file=self.buka.replace("exec","decompyy=")
		self.potong=sys.argv[1].replace(".py","_dec.py")
	def decompyy(self):
			if "marshal.loads" in self.buka:
				try:
					if "exec" not in self.buka:keluar("{}[{}!{}]{} File {} Exec Not Detected".format(merah,hijau,merah,putih,sys.argv[1]))
					else:
						open(".cache","w").write("merah, hijau, putih='\\x1b[1;31m', '\\x1b[1;32m','\\x1b[1;37m'\nfrom uncompyle6.main import decompile as dec\nfrom sys import stdout as aapgans\n"+self.file+"\ntry:\n    dec(2.7,decompyy,aapgans)\nexcept Exception as xnxx:\n    exit('{}[{}!{}]{} Error : {}'.format(merah,hijau,merah,putih,str(xnxx)))") ; os.system("python2 .cache > "+self.potong) ; df=open(self.potong).read() ; open(self.potong,"w").write(" ")
						if "import" in df or "from" in df or "print" in df or "time.sleep" in df or "hex" in df or "print" in df or "os" in df or "sys" in df or "=" in df or "'" in df or '"' in df or "(" in df or ")" in df:os.remove(".cache") ; keluar("{}[{}✓{}]{} File Saved As : {}".format(hijau,cyan,hijau,putih,self.potong))
						else:os.remove(".cache");keluar("{}[{}!{}]{} Decompyle Failed!".format(merah,hijau,merah,putih))
				except Exception as exx:keluar(str(exx))
			elif "marshal.loads" not in self.buka:
				try:
					if "exec" not in self.buka:keluar("{}[{}!{}]{} File {} Exec Not Detected".format(merah,hijau,merah,putih,sys.argv[1]))
					else:
						open(".cache","w").write(self.file+"\nmerah, hijau, putih='\x1b[1;31m', '\x1b[1;32m','\x1b[1;37m'\n\ntry:\n    print(decompyy)\nexcept Exception as xnxx:\n    exit('{}[{}!{}]{} Error : {}'.format(merah,hijau,merah,putih,str(xnxx)))") ; os.system("python2 .cache > "+self.potong) ; df=open(self.potong).read() ; open(self.potong,"w").write(" ")
						if "import" in df or "from" in df or "print" in df or "time.sleep" in df or "hex" in df or "print" in df or "os" in df or "sys" in df or "=" in df or "'" in df or '"' in df or "(" in df or ")" in df:os.remove(".cache") ; keluar("{}[{}✓{}]{} File Saved As : {}".format(hijau,cyan,hijau,putih,self.potong))
						else:os.remove(".cache");keluar("{}[{}!{}]{} Decompyle Failed!".format(merah,hijau,merah,putih))
				except Exception as exx:keluar(str(exx))
if __name__=="__main__":
	ver="2.7"
	if platform.python_version().split(".")[0] != "2":
		keluar("\x1b[1;31m[\x1b[1;32m!\x1b[1;31m] \x1b[1;37mUse Python %s Version"%ver.split(" ")[0])
	try:
		kansnsnsnsnnsbebensmamamalalalaknwbwbwksnwvrvyctvrjsknsjdudjsjsjebebbebenenen_hdjdndndnjsnsnsn_jsjsnsnsmmemememsnsjdjdjsbsbsjaoaoqowisuusjw=decompy(sys.argv[1])
		kansnsnsnsnnsbebensmamamalalalaknwbwbwksnwvrvyctvrjsknsjdudjsjsjebebbebenenen_hdjdndndnjsnsnsn_jsjsnsnsmmemememsnsjdjdjsbsbsjaoaoqowisuusjw.decompyy()
	except IndexError:
		keluar("{}[{}!{}] {}Usage : python2 {} file.py".format(merah,hijau,merah,putih,sys.argv[0]))
	except IOError:
		keluar("{}[{}!{}] {}File {} Not Found".format(merah,hijau,merah,putih,sys.argv[1]))
