#
# Juego4enLineaEquipo07.py
#
# DESCRIPCION: algoritmo que permite a un usuario jugar al 4 en linea \
# contra una IA con 2 niveles de di cultad (facil y medio), a traves de la \
# terminal de la interfaz gra ca.
#
# Autores: 
#	Br. Jose Barrera y Alfredo Cruz.
#
# Ultima m i cacion: 16/03/2018.

"""
   CONS					# las constantes nos ayudan a tener la informacion que no
   	nombre : str  			# p emos pedir al usuario, su nombre, la di cultad, 
	nivel : int  			# si desea abandonar una partida, si desea salir del programa,
	rendirse : bool  		# y por supuesto la jugada que hara en cada turno reflejada en
	irse : bool  			# sus coordenadas  la, columna.
	x : int  
	y : int  
	N : int  			# Numero de  las 	# estas son las verdaderas constantes del programa
	M : int  			# Numero de columnas
   VAR
	A : array [0..N)x[0..M) of int  	# el tablero de juego
	jugando : bool  			# en partida
	turno : int  				# contador de los turnos 
	juega : int  				# a quien le toca jugar(True para user, False para IA)
	ganador : int  				# el primero en cumplir las condiciones
	dentro : bool  				# dentro del programa
	movida : bool  				# permite reintentar hasta hacer una jugada
	i : int  				#  la jugada de la IA 
	j : int  				# columna jugada de la IA
	partida : int   			# numero de partidas jugadas en sesion actual
	bound : int  				# cota que permite que los ciclos terminen
"""	
|	#Precondicion
	assert( N = 6 and M = 7 )
		
	jugando,turno,ganador,juega,dentro,partida:False,1,0,True,True,1	#Incializacion de las variables
		
	{bound = 43 - turno}
		
	while dentro :									#en menu
		if not(jugando) :
			resultados( ganador )
			terminar( irse )
			if nuevapartida( decision , partida )
			Inicio(A)
	
		elif jugando :							#en partida
			if turno = 43 :
				jugando=0					# el tablero se encuentra lleno, se declara empate
			elif turno < 43 :						
				if juega :					# juega=True representa al usuario
					abandonar(rendirse)  			# en cada turno el usuario debe decidir si sigue la partida actual  
					jugadaUser(A,x,y)  
				elif not(juega) :
					if nivel = 1 :					# el nivel 1 hace un random de todas las
						movida=True  				# las coordenadas del tablero hasta 
						while movida:				# encontrar una jugada valida
							i=random.randrange(6)		
							j=random.randrange(7)
							if valida(A,i,j) :
								A[i][j] = 2
								movida = False		# momento en el que se rompe el ciclo
						victoria(A,i,j)  
					
					elif nivel = 2 :				# el nivel 2 presenta una sencilla IA
						if turno=1 \/ turno=2 :			# que lo hace apenas mas complejo
							if valida(5,3):		
								A[5][3]=2		# se le da una jugada inicial predefinida
								i,j=5,3 				
							elif not (valida(5,3)):		# y una jugada alternativa
								A[5][2]=2
								i,j=5,2  
							   
						elif turno > 2 :			# a partir de una jugada anterior
							IA(A,i,j)  			# decide que linea deberia jugar
							victoria(A,i,j)  
					 
				turno = turno + 1
				juega = not(juega)
					 
				   
			 
   { dentro = False }
]

#Aqui termina el esqueleto del programa, de aqui en adelante se colocan
# t os los procedimientos que llama.

def jugadaUser( x = int , y = int, A= array [0..6)x[0..7) of int )   
	#Pre: True 
	# Post:  (valida(x,y)=1 => A[x][y] = 1]) and (valida(x,y)=0 => A[x][y] = 0) 
	#VAR
	#ganador : int  
	#jugando : bool

	ganador = 0
	jugando = True
		
	while True :
		if valida(x,y):
			A[x][y] = 1
			victoria(A,x,y)
			break
		else not valida(i,j):			#se pide al usuario que intente otra jugada
			print("Jugada no valida,intenta otra vez")
	return A

# Esta es la funcion una de las funciones mas importantes del programa, sin importar
# si la coordenada esta o no en el tablero (la matriz A), nos dice si la jugada es valida
def valida( A = array [0..6)x[0..7), i=int, j=int ) : bool
	#Pre: True 
	#Post: valida=((A[i][j]=0)andi=5)\/((A[i][j]=0)andi<5andA[i-1][j]!=0)
	#VAR:
	#valida : bool  
	
	if 0 <= i < 6 and 0 <= j < 7: 
		if A[i][j]=0:
			if i=5:
				valida=True
			elif i<5 and A[i-1][j]!=0:
				valida=True
			elif i<5 and A[i-1][j]=0:
				valida=False
			
		else A[i][j]!=0:
			valida=False
		
	elif i < 0 or i > 5 or j < 0 or j > 6:
		valida=False
	

	return valida
		
def victoria( A= array [0..6)x[0..7), i=int,j= int)            
	#Pre: True  
	# Post:  (ganador=0 and jugando=1) \/ ((ganador=1 \/ ganador=2)and(jugando=0))

	victoriahorizontal(A,i,j)  

	if jugando:
		victoriavertical(A,i,j)
		if jugando:
			victoriadiagonalprincipal(A,i,j)
			if jugando:
				victoriadiagonalsecundaria(A,i,j)
			elif not(jugando:
				pass
		elif not jugando:
			pass
		
	elif not jugando:
		pass
	
	return (ganador,jugando)

#Aqui se veri can las distintas condiciones para que un jugador gane el juego formando 4 en raya.
def victoriadiagonalprincipal( A = array [0..6)x[0..7)   in i,j = int)      
	#Pre: N = 6 and M = 7  
	# Post:  (ganador=0 and jugando=1) \/ ((ganador=1 \/ ganador=2)and(jugando=0)) 
	#VAR
    	#ganador : int  
		#jugando : bool  
		#i : int  
		#j : int  

	jugando = True

	i=0
	#cota= 6-i
	while i < 3:
		j=0
		#cota= 4-j
		while j < 4 and jugando=True:
			#Conexion diagonal principal
			if A[i][j]=A[i+1][j+1]=A[i+2][j+2]=A[i+3][j+3]=1:
				ganador=1
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
			
			elif A[i][j]=A[i+1][j+1]=A[i+2][j+2]=A[i+3][j+3]=2:
				ganador=2
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
			j=j+1
		i=i+1
	return (ganador,jugando)

def victoriahorizontal( A = array [0..6)x[0..7)   i=int, j= int)          
	# Pre: N = 6 and M = 7  
	# Post:  (ganador=0 and jugando=1) \/ ((ganador=1 \/ ganador=2)and(jugando=0)) 
	#VAR
    	#ganador : int  
		#jugando : bool  
		#i : int  
		#j : int  

	jugando,i = True,0

	#cota=6-i
	while i<6:
		j=0
		#cota=4-j}
		while j<4 and jugando=True:
			#Conexion horizontal
			if A[i][j]=A[i][j+1]=A[i][j+2]=A[i][j+3]=1:
				ganador=1
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3

			elif A[i][j]=A[i][j+1]=A[i][j+2]=A[i][j+3]=2:
				ganador=2
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
			j=j+1
		i=i+1
	return (ganador,jugando)


proc victoriavertical( A = array [0..6)x[0..7), i=int, j = int)             
	# Pre: N = 6 and M = 7  
	# Post:  (ganador=0 and jugando=1) \/ ((ganador=1 \/ ganador=2)and(jugando=0)) 
	#VAR
    	#ganador : int  
		#jugando : bool  
		#i : int  
		#j : int  

	jugando, i = True,0

	#cota= 3-i
	while i < 3:
		j=0
		#cota= 7-j
		while j < 7 and jugando=1:
			if A[i][j]=A[i+1][j]=A[i+2][j]=A[i+3][j]=1:
				ganador=1
				jugando=0
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
			elif A[i][j]=A[i+1][j]=A[i+2][j]=A[i+3][j]=2:
				ganador=2
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3
			
			j=j+1
		i=i+1
	return (ganador,jugando)


def victoriadiagonalsecundaria( A = array [0..6)x[0..7)   i=int, j=int)       
	#Pre: N = 6 and M = 7  
	# Post:  (ganador=0 and jugando=1) \/ ((ganador=1 \/ ganador=2)and(jugando=0)) 
	#VAR
    #	ganador : int  
	#	jugando : bool  
	#	i : int  
	#	j : int  

	jugando, i = True, 0

	
	#cota=3-i
	while i < 3:
		j=0
		#cota=7-j
		while j < 7 and jugando=True:
			#Conexion diagonal secundaria
			if j>2 and A[i][j]=A[i+1][j-1]=A[i+2][j-2]=A[i+3][j-3]=1:
				ganador=1
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3

			elif j>2 and A[i][j]=A[i+1][j-1]=A[i+2][j-2]=A[i+3][j-3]=2:
				ganador=2
				jugando=False
				A[i][j],A[i+1][j+1],A[i+2][j+2],A[i+3][j+3]=3,3,3,3

			j=j+1
		i=i+1
	return (ganador,jugando)

# Aqui culminan las veri caciones de las posibilidades de ganar el juego con un 4 en raya.

def Inicio( A= array [0..6)x[0..7) of int) 		#tambien arroja el nombre y la di cultad
	#Pre: True
	#Post: (%forall i,j : 0<=i<6 and 0<=j<7 : A[i][j])}
   	#VAR:
	#A : array [0..6)x[0..7) of int  
	#i : int  
	#j : int  
	#nombreusuario:"Coloque su nombre, por favor:")  
	#di cultad:"Seleccione la di cultad:(1=basico,2=medio)"

	i=0
	#cota= 6-i
	while i<6:
		j=0
		#cota= 7-j
		while j<7:
			A[i][j]=0
			j=j+1
		i=i+1
	return (A)	


def nuevapartida( decision = bool , partida= int )   
	#Pre: True
	#Post:irse=>jugando=False and not irse=>jugando=True

	#se le pregunta al usuario si desea o no volver a jugar o no, esto
	#se almacena en la variable de entrada decision y cambia el valor
	#de jugando
	if decision:
		jugando=True
		partida=partida+1
	elif not decision:
		pass                  #se sale del juego
	
	return(partida,jugando)


def resultados(ganador=int, partida = int)              
	#Pre: ganador==0 \/ ganador==1 \/ ganador==2
	#Post: G[0]+G[1]+G[2]= partida-1
	#VAR:
	#ganador:int  
	#G: array [0..2) of int  				# la tabla de resultados se muestra al usuario
							# mientras no esta jugando
	G=(0 for i in range (0,3))

	if partida=1:
		G[0]=-1
		G[1]=0
		G[2]=0
	elif ganador=0:
		G[0]=G[0]+1
		juega = False
	elif ganador=1:
		G[1]=G[1]+1
		juega = True
	elif ganador=2:
		G[2]=G[2]+1
		juega = True
	
	return(G,juega)


def abandonar( irse= bool, jugando= bool)   
	#Pre: jugando=True
	#Post: irse=>jugando=False and not irse=>jugando=True
	#este procedimiento toma la decision del usuario, reflejada en la constante irse
	#y m i ca el valor de jugando para terminar o continuar la partida

	if irse:
		jugando=False
	elif not irse:
		pass
	
	return (jugando)


def terminar( rendirse= bool, dentro= bool)
	#Pre: dentro=True
	#Post: rendirse=>dentro=False and not rendirse=>dentro=True

	#este procedimiento toma la decision del usuario, reflejada en la constante terminar
	#y m i ca el valor dentro para salirse o no del programa 

	if rendirse:
		dentro=False
	elif not rendirse:
		pass

	return (dentro)	
	


def IA( i=int,j=int , A=() )
	#Pre: 0<=i<6 and 0<=j<7
	#Post: 0<=i<6 and 0<=j<7

	#VAR:					# para esta primera version de la IA solo nos interesan
	#x:int  					# las que puede hacer a partir de la anterior, por lo que
	#max:int  				# la vi(vertical inferior queda descartada), y tiende a
	#hi,hd,vs,dps,dss: int  			# escoger jugadas horizontales.

	hi,hd,vs,dps,dpi,dss,dsi=0,0,0,0,0,0,0  
								
	x=1				# aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota= 4-x			# linea horizontal hacia la izquierda de su posicion
	while x<4 and valida(i,j-x): 	
		hi= hi+1		
		x=x+1

	x=1				    # aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota= 4-x			# linea horizontal hacia la derecha de su posicion
	while i<4 and valida(i,j+x):
		hd= hd+1
		x=x+1

	
	if valida(1+x,j):		# aqui solo se cuenta si la proxima posible jugada para armar una
		vs = vs+1		    # linea vertical, justo arriba de su posicion
	elif not valida(1+x,j):
		pass

	x=1				        # aqui cuenta las 3 proximas posibles jugadas para armar una	
	#cota= 4-x				# linea diagonal principal superior (raro pero posible)
	while x<4 and valida(i-x,j-x):	 
		dps= dps+1
		x=x+1


	x=1				        # aqui cuenta las 3 proximas posibles jugadas para armar una	
	#cota= 4-x				# linea diagonal principal inferior (raro pero posible)                
	while x<4 and valida(i+x,j+x):	 
		dpi= dpi+1
		x=x+1
	

	x=1	     			    # aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota= 4-x			    # linea diagonal secundaria superior (raro pero posible)
	while x<4 and valida(i-x,j+x):
		dss= dss+1
		x=x+1

	
	x=1				# aqui cuenta las 3 proximas posibles jugadas para armar una
	#cota=4-x			# diagonal secundaria inferior (raro pero posible)
	while x<4 and valida(i+x,j-x):
		dsi= dsi+1
		x=x+1
	

	max=max(hi,hd,vs,dps,dpi,dss,dsi)  	# buscamos la jugada mas "favorable"
		if max=0:			# si la pieza se encuentra r eada, se busca un nuevo
			i,j=5,6		# lugar donde jugar.
			#cota=i
			while 0 <= i < 6:
			#cota= j
				while 0 <= j < 7:
					if valida(i,j):
						A[i][j]=2
					elif not valida(i,j):
						pass
					j=j-1
				i=i-1
			
		elif max=hi:			# la ejecutamos
			A[i][j-1]=2
		elif max=hd:
			A[i][j+1]=2
		elif max=vs:
			A[i+1][j]=2
		elif max=dps:
			A[i][j+1]=2
		elif max=dpi:
			A[i][j+1]=2
		elif max=dss:
			A[i][j+1]=2
		elif max=dsi:				
			A[i][j+1]=2

	return (i,j,A)		
		
# Se planea mejorar esta IA, para que reconozca si esta r eada de jugadas aliadas o rivales
# de tal manera que pueda mejorar aun mas su criterio de decision.
# Posible nivel 3
