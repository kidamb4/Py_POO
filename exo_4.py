from abc import abstractmethod,ABC 
# Un nombre est premier quand on ne peut le diviser que par 1 et lui-même. Sauf 1 par convention. 
# Exemple : 3 
# Un nombre est parfait quand il est égal à la somme de ses diviseurs. 
# Exemple : 6 = 1 + 2 + 3 



# Fonctions à implémenter dans les méthodes 
def is_prime(n): 
	"""Indique si n est premier """                                                   
	for i in range(2, (n//2+1)):
		if (n % i) == 0:
			return False                                                    
	return True
#print(is_prime(2))
#print(is_prime(3))

def is_perfect(n):
	"""Indique si n est parfait"""
	r = list() # stocker les diviseurs de n
	for k in range(2,(n//2+1)):
		if (n % k == 0) and (k not in r):
			r.extend([k,n//k])# Ajout de diviseurs (si 2 est divseur de 6 alors 6//2 == 3 aussi.)
	return sum(r)+1 == n 

# print(is_perfect(6))
# print(is_perfect(10))

class Number(ABC):
	def __init__(self,results = list()):
		super().__init__()
		self.results = results

	@abstractmethod
	def __isprime(self):
		pass

	@abstractmethod
	def __isperfect(self):
		pass

	@abstractmethod
	def __read_number(self):
		pass


class FooNumber(Number):
	def __isprime(self,n):
		"""isprime sera implémentée à l'aide d'une boucle while"""
		i = 2
		while i <= (n//2):
			if (n % i) == 0:
				return False
			i += 1
		return True

	def __isperfect(self,n):
		"""isperfect sera implémentée à l'aide d'une boucle while"""
		r = list() ; k = 2 # stocker les diviseurs de n 
		while k <= (n//2):
			if (n % k == 0) and (k not in r):
				r.extend([k,n//k])
			k += 1
		return sum(r)+1 == n 

	def __read_number(self,n):
		"""demande à l'utilisateur de saisir un nombre puis renvoie ce nombre"""
		return n

	def check(self,n):
		"""vérifie si le nombre est premier, parfait, puis stocke le résultat dans result"""
		if self.__isprime() or self.__isperfect():
			self.results.append(n)

class BarNum(Number):
	def __isprime(self,n):
		"""isprime sera implémentée à l'aide d'une boucle for"""
		for i in range(2, (n//2+1)):
			if (n % i) == 0:
				return False
		return True
		
	def __isperfect(self,n):
		"""isperfect sera implémentée à l'aide d'une boucle for"""
		r = list() # stocker les diviseurs de n
		for k in range(2,(n//2+1)):
			if (n % k == 0) and (k not in r):
				r.extend([k,n//k])
		return sum(r)+1 == n 

	def __read_number(self):
		"""lit le nombre depuis un fichier puis renvoie ce nombre"""
		file = open("fichier.txt","r")
		return file.read(1)
	def check(self):
		"""vérifie si le nombre est premier, parfait, puis stocke le résultat dans results"""
		n = open("fichier.txt","r").read(1)
		if self.__isprime() or self.__isperfect():
			self.results.append(n)



f1 = FooNumber([])
f1.check(6)
f1.check(7)
print(f1.results,sep='\n')

b1 = BarNum()
b1.check()
print(b1.results, sep='\n')
		

