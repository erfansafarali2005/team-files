class Darookhaneh:
    print('be darookhaneh doctor zamani khosh amadid ☆*: .｡. o(≧▽≦)o .｡.:*☆')
    esm = 'darookhaneh doctor zamani'
    mogheiat = 'lorestan_khoram abad'
    darooha = []
    bimaran = []
    karmandane_faal = []
    karmandan = []
    liste_noskheha = []
    daramade_khales = 0

    @staticmethod
    def etelaat():
        return f'be {Darookhaneh.esm} dar {Darookhaneh.mogheiat} khoshamadid ╰(*°▽°*)╯'
    
    def kharide_daroo(daroo):
        Darookhaneh.daramade_khales += daroo.gheimat
        print(f'shoma darooye {daroo.esm} ra be gheimate {daroo.gheimat} toman kharidary kardid o(*￣▽￣*)ブ')

class Daroo:
    def __init__( self , esm , sal , engheza , gheimat ):
        self.esm = esm
        self.sal = sal
        self.engheza = engheza
        self.gheimat = gheimat
        if self not in Darookhaneh.darooha:
            Darookhaneh.darooha.append(self)
        
    @classmethod
    def init( cls , esm , sal , gheimat ):
        engheza = 2024 - sal
        return cls( esm , sal , engheza , gheimat )
    def __str__(self):
        return f'esm: {self.esm} sal: {self.sal} enhgeza: {self.engheza} sal, gheimat: {self.gheimat}'
    
class Karmand:
    def __init__( self , esm , famili , shomareh ):
        self.esm = esm
        self.famili = famili
        self.shomareh = shomareh
        self.faal = True

        Darookhaneh.karmandan.append(self)
        Darookhaneh.karmandane_faal.append(self)

    @staticmethod
    def namayeshe_bimaran():
            return f'liste bimaran (≧∀≦)ゞ : {[str(bimar) for bimar in Darookhaneh.bimaran]}'  
    @staticmethod
    def amayeshe_darooha():
        liste_darooha = [f'{daroo.esm}: {daroo.gheimat}' for daroo in Darookhaneh.darooha]
        return f'liste darooha ( $ _ $ ) : {liste_darooha}'
    @staticmethod
    def amayeshe_noskheha():
        return f'liste noskheha (✿◠‿◠) : {Darookhaneh.liste_noskheha}'
    @staticmethod
    def amayeshe_daramad():
        return f'daramade khales ( $ _ $ ) : {Darookhaneh.daramade_khales}'
        
    def afzoodane_daroo( self , *args ):
        for daroo in args:
            if daroo not in Darookhaneh.darooha:
                Darookhaneh.darooha.append(daroo)
                print(f'darooye ezafe shodeh ( •̀ ω •́ )y : {daroo.esm}')

    def morakhassy(self):
        try:
            if self.faal:
                Darookhaneh.karmandane_faal.remove(self)
                self.faal = False
                print('morakhassy khosh begzare ( •̀ ω •́ )✧')
        except:
            print('to ke hanoo narafty ://////////////////')

    def bargasht_az_morakhassy(self):
        if not self.faal:
                Darookhaneh.karmandane_faal.append(self)
                self.faal = True
                print('khosh bargastty mashty (￣y▽￣)╭ Ohohoho.....')
        else:
            print('gereftimoon?? o((>ω< ))o')

    def __str__(self):
        return f'{self.esm} {self.famili} ^^^^^^^ shomareh: {self.shomareh}'

class Bimar:
    noskheha = []
    def __init__( self , esm , famili , shomareh ):
        self.esm = esm
        self.famili = famili
        self.shomaref = shomareh
        Darookhaneh.bimaran.append(self)

    def dadane_noskhe( self , noskhe ):
        self.noskheha.append(noskhe)
        Darookhaneh.liste_noskheha.append(noskhe)
        print (f'noskhe ezafe shodeh (((o(*ﾟ▽ﾟ*)o))) : {noskhe}')
        print (Darookhaneh.liste_noskheha)

    def __str__(self):
        return f'{self.esm} {self.famili} ^^^^^^^ shomareh: {self.shomaref}'
    
daroo1 = Daroo.init('Albendazole (600)' , 2023 , 1900)
daroo2 = Daroo.init('Tylosin (20%)' , 2022  , 45000)
daroo3 = Daroo.init('Enrofloxacin (10%)' , 2023 , 70000)
daroo4 = Daroo.init('Cupermetrin (10%)' , 2023 , 80000)
daroo5 = Daroo.init('Vita (tazrighy,20cc)' , 2023 , 35000)
daroo6 = Daroo.init('Oxytetracycline 500 (razak)' , 2023 , 1800000)
daroo7 = Daroo.init('Butalex (50cc)' , 2023 , 219000)
daroo8 = Daroo.init('Vitamina zene (7%)' , 2023 , 180000)
daroo9 = Daroo.init('Peniciline Streptomicine (2+2)' , 2023 , 25700)
daroo10 = Daroo.init('Sulfadine' , 2023 , 930000)

karmand = Karmand('Enayat' , 'Shahrokhy' , '+989128694063')
karmand.afzoodane_daroo(daroo1,daroo2,daroo3,daroo4,daroo5,daroo6,daroo7,daroo8,daroo9,daroo10)
print(Karmand.amayeshe_darooha())
print('○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…')
Darookhaneh.kharide_daroo(daroo1)
Darookhaneh.kharide_daroo(daroo2)
Darookhaneh.kharide_daroo(daroo3)
Darookhaneh.kharide_daroo(daroo4)
Darookhaneh.kharide_daroo(daroo5)
Darookhaneh.kharide_daroo(daroo6)
Darookhaneh.kharide_daroo(daroo7)
Darookhaneh.kharide_daroo(daroo8)
Darookhaneh.kharide_daroo(daroo9)
Darookhaneh.kharide_daroo(daroo10)
print('○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…')
bimar1 = Bimar('mohammad' , 'mousivand' , '+989939476400')
bimar1.dadane_noskhe('avalin noskhe (✿◠‿◠)')
print('○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…')
print(Karmand.namayeshe_bimaran())
print(Karmand.amayeshe_noskheha())
print(Karmand.amayeshe_darooha())
print(Karmand.amayeshe_daramad())
print('○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…')
karmand.morakhassy()
karmand.bargasht_az_morakhassy()
print('○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…○( ＾皿＾)っ Hehehe…')
print('kheylyyyyyyyyyyyyyyyy khodaaaaaaaaaaaaaaaa negaddarrrrrrrrrrrrrrr')