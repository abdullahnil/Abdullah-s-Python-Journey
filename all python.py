#print komutu ile birlikte nşa istediğim gibi yazabiliyorum
print ('Bismillah. Bu Python dosyasının kodlarında açıklamalar bulunmaktadır. ')
print ('')
print ('c Hiçbir hakkı Abdullah Nil e ait değildir.')
print('Ders Kaynağı: https://introcs.cs.princeton.edu/python/home/')
print('Öğrenci Websitesi (Daha HTML Bilmiyor): https://abdullahnil.net')
print('')
print ('-------Kaynak Kodlarında Bulunan Açıklamalar--------')
print ('1)Miniconda Komutları')
print ('2)Program Execute Etmek')
print ('3)Dışarıdan Kod Import Etmek')
print('')
print('')
print('')
print('---Hocaya sorulacaklar---')
print ('1)Eğer yazıda tırnak işaretini kullanacaksak, nasıl kullanabiliriz?')
print('2)Dosya adlarında boşluk bırakırsak, execute edemez miyiz?')

#------Miniconda komutları--------#
#Az sonra yazacağım komutlar, miniconda'ya girilen komutlardandır.
#Toplu olması için buraya ekliyorum.
#conda create –name python
#conda create -n python
#conda activate
#conda deactivate
#conda info –envs
#conda remove -n deneme3.12.5 --all

#-----Program Execute Etmek-----#
#Eğer bu kodları kullanmak istersen, bunların yüklü olduğu klasörü açıp
#Terminal üzerinden  python all python.py yazman yeterli.



print('')


#-------Dışarıdan kod import etmek--------#
#  Bu stdio dediğimiz nanedeki amaç, dışarıdan library yüklüyoruz ve
# onu buraya import ederek kod keşmekeşinden kaçıyoruz :)
import stdio
stdio.writeln ('Stdio çalıştı')
print('')


#https://introcs.cs.princeton.edu/python/11hello/ Input and Output kısmında kaldım.

import sys

stdio.write('Hi, ')
stdio.write(sys.argv[1])
stdio.writeln('. How are you?')


