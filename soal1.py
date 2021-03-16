class persegi():
    def __init__(self,x):
        self.sisi = x
        
    def luas(self,x):
        self.luas = x**2
        return self.luas
    
    def keliling(self,x):
        self.kel = 4*x
        return self.kel

x = int(input('Masukkan Sisi Persegi: '))
n = persegi(x)
L = n.luas(x)
K = n.keliling(x)
print('Luas Persegi Dengan Panjang Sisi 100 Adalah:',L)
print('Keliling Persegi Dengan Panjang Sisi',x,'Adalah:',K)
print()