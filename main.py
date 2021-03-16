# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)

###### exercice 01
def makeDico_G1(nomFichier, sep):
      fichier = open(nomFichier, 'r');
      dico ={};
      while 1:
        ligne = fichier.readline(); # lecture d'une ligne du fichier
        if ligne == "" or ligne == "\n" :
          break
        x = ligne.split(sep);
        dico[x[0]] = x[1];
      return dico;

###### exercice 02
def verifUrl_C3(url):
      x = url.split('.');
      if(len(x) == 2):
        if(len(x[1]) < 4):
          return True;
        else:
          print('url mal formee');
          return False;
      else:
        print('url mal formee');
        return False;

###### exercice 03
def getTLD_Q3(url):
      x = verifUrl_C3(url);
      if(x == False):
        print('TLD mal formee');
        return False;
      else:
        a = url.split('.');
        print(a[1]);

###### exercice 04
def VerifTLD_N6(tldOk,'tld'):
      if()

###### exercice 05
    

###### exercice 06


# Zone 2 ## zone pour les classes
###### exercice 07


###### exercice 08


###### exercice 09
    

# Zone 3 ## zone pour les tests des fonctions


