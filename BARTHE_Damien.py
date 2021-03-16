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
          return False;
      else:
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

def main() :
	from re import split
	###### exercice 00 (la fonction est appelee dans cette zone afin de confirmer son fonctionnement)
	print("exercice 00 #######################")
	salutations = exempleHello("Michel")
	print(salutations)
	print(salutations.split(sep=" "))

	###### exercice 01
	print("exercice 01 #######################")

	###### exercice 02
	print("exercice 02 #######################")


	###### exercice 03
	print("exercice 03 #######################")


	###### exercice 04
	print("exercice 04 #######################")


	###### exercice 05
	print("exercice 05 #######################")


	###### exercice 06
	print("exercice 06 #######################")

	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
	print("exercice 07 #######################")


	###### exercice 08
	print("exercice 08 #######################")


	###### exercice 09
	print("exercice 09 #######################")
	
	###### exercice 10
	print("exercice 10 #######################")

if __name__=="__main__":
	print("main()")
	main()