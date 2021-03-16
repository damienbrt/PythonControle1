# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)
def exempleHello (msg):
    return "bonjour {}, comment allez-vous ?".format(msg)


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
def VerifTLD_N6(tldOk,tld):
      if(tld in tldOk):
        return True
      else :
        print('TLD absente');
        return False;

###### exercice 05
def ipVerifFormat_U6(adresseIp):
      result = 0;
      x = adresseIp.split('.');
      if(len(x) == 4):
        for i in [0, 1, 2, 3]:
          if(x[i] in range(0,256)):
            result = result + 1;
            print(x[i]);
        if(result == 4):
          return True;
        else:
          print("Champ d'adresse incorrect")
          return False;
      else:
        print('Nombre de champ incorect');
        return False;

###### exercice 06
def makeTLD_A7(dico):
      liste = [];
      for key, value in dico.items():
        if(getTLD_Q3(key) not in liste):
          liste.append(getTLD_Q3(key))
      return liste;

# Zone 2 ## zone pour les classes
###### exercice 07
class serveurDns_F6:
  def __init__(self, resolDns):
    self.resolDns = resolDns;

###### exercice 08
class serveurDns_F6:
  def __init__(self, resolDns):
    self.resolDns = resolDns;
  
  def resoldDNS_M4(self,url):
    if(verifUrl_C3(url)):
      for key, value in self.resolDns.items():
        if(url in key):
          return True;
        else:
          print('Url introuvable')
          return False;
    else:
      print("Erreur de format de l'url");
      return False;
###### exercice 09
class serveurDns_F6:
  def __init__(self, resolDns):
    self.resolDns = resolDns;
  
  def resoldDNS_M4(self,url):
    if(verifUrl_C3(url)):
      for key, value in self.resolDns.items():
        if(url in key):
          print(value);
          return True;
        else:
          print('Url introuvable')
          return False;
    else:
      print("Erreur de format de l'url");
      return False;
    
  def resolInverse_X8(self,adresseIp):
    if(ipVerifFormat_U6(adresseIp)):
      for key, value in self.resolDns.items():
        if(adresseIp in value):
          print(key)
          return True;
        else:
          print('adresseIp introuvable')
          return False;
    else:
      print("Erreur de format de l'adresse IP");
      return False;
###### exercice 10
class serveurDns_F6:
  def __init__(self, resolDns):
    self.resolDns = resolDns;
  
  def resoldDNS_M4(self,url):
    if(verifUrl_C3(url)):
      for key, value in self.resolDns.items():
        if(url in key):
          print(value);
          return True;
        else:
          print('Url introuvable')
          return False;
    else:
      print("Erreur de format de l'url");
      return False;
    
  def resolInverse_X8(self,adresseIp):
    if(ipVerifFormat_U6(adresseIp)):
      for key, value in self.resolDns.items():
        if(adresseIp in value):
          print(key)
          return True;
        else:
          print('adresseIp introuvable')
          return False;
    else:
      print("Erreur de format de l'adresse IP");
      return False;
  
  def addAsso_K4(self,url,adresseIp):
    if(self.resolInverse_X8(adresseIp)):
      if(self.resoldDNS_M4(url)):
        dico = makeDico_G1('dns.txt', ',')
        if(adresseIp not in dico):
          if(url not in dico):
            dico[url] = adresseIp;
            return True;
          else:
            print('existingURL');
        else:
          print('existingIP');
      else:
        print('malformedAddress');
    else:
      print('malformedAddress');
# Zone 3 ## zone pour les tests des fonctions

def main() :
	from re import split
	###### exercice 00 (la fonction est appelee dans cette zone afin de confirmer son fonctionnement)
	print("exercice 00 #######################")
	salutations = exempleHello("Michel")
	print(salutations)
	print(salutations.split(sep=" "))

	###### exercice 01
	print("exercice 01 #######################")
  makeDico_G1('dns.txt',',')
	###### exercice 02
	print("exercice 02 #######################")
  verifUrl_C3('google.fr')

	###### exercice 03
	print("exercice 03 #######################")
  getTLD_Q3('google.fr')

	###### exercice 04
	print("exercice 04 #######################")

	###### exercice 05
	print("exercice 05 #######################")
  ipVerifFormat_U6('1111111.1111111.1111111.1111111')

	###### exercice 06
	print("exercice 06 #######################")
  makeTLD_A7(makeDico_G1('dns.txt',','))

	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
	print("exercice 07 #######################")
  s = serveurDns_F6(makeDico_G1('dns.txt',','))

	###### exercice 08
	print("exercice 08 #######################")
  s = serveurDns_F6(makeDico_G1('dns.txt',','))
  s.resoldDNS_M4('gooqsdqsd')
  s.resoldDNS_M4('google.fr')

	###### exercice 09
	print("exercice 09 #######################")
	s = serveurDns_F6(makeDico_G1('dns.txt',','))
  s.resolInverse_X8('193.164.196.17')

	###### exercice 10
	print("exercice 10 #######################")
  s.addAsso_K4('goooooogle.fr','111.111.111.111')
  
if __name__=="__main__":
	print("main()")
	main()