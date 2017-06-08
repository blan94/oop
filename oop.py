import os
import shutil
os.chdir("/home")
os.mkdir("./cellar")
os.mkdir("./myhouse")
print "cellar ve myhouse klasorlerini olusturma basarili"
dosol = open("/home/myhouse/nolongeraplanet.txt","w")
dosol.write("Pluto*")
dosol.close()
print "nolongeraplanet.txt dosyasi olusturuldu icine Pluto* eklendi"
src = "/home/myhouse/nolongeraplanet.txt"
dst = "/home/myhouse/~.txt"
os.symlink(src,dst)
print "sembolik link olusturma basarili"
sr = "/home/myhouse/~.txt"
ds = "/home/cellar/"
shutil.copy2(sr,ds)
sre = "/home/myhouse/nolongeraplanet.txt"
shutil.copy2(sre,ds)
print "kopyalama islemi basarili"
os.chmod("/home/myhouse/nolongeraplanet.txt",0400)
print "sadece user icin okuma yetkisi verildi"
print ""
print "asagidaki kodu kopyala/yapistir yap"
print "users | grep 'Adam' | sort -u | wc -l > /home/storage/thelist.txt"
print "islem bu kadar :)"
