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


