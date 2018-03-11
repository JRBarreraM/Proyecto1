A=[[0]*7]*6
#1 REPRESENTS: PLAYER
#2 REPRESENTS: IA
#0 REPRESENTS: TIE
def verificar(A: array) -> (int,int):
	for i in range(6):
		for j in range(4):
			#Conexion diagonal principal
			if i<3 and A[i][j]==A[i+1][j+1]==A[i+2][j+2]==A[i+3][j+3]==1:
				winner=1
				jugando=0	
			elif i<3 and A[i][j]==A[i+1][j+1]==A[i+2][j+2]==A[i+3][j+3]==2:
				winner=2
				jugando=0
			#Conexion horizontal
			elif A[i][j]==A[i][j+1]==A[i][j+2]==A[i][j+3]==1:
				winner=1
				jugando=0
			elif A[i][j]==A[i][j+1]==A[i][j+2]==A[i][j+3]==2:
				winner=2
				jugando=0
	for i in range(3):
		for j in range(7):
			#Conexion diagonal secundaria
			if j>2 and A[i][j]==A[i+1][j-1]==A[i+2][j-2]==A[i+3][j-3]==1:
				winner=1
				jugando=0
			if j>2 and A[i][j]==A[i+1][j-1]==A[i+2][j-2]==A[i+3][j-3]==2:
				winner=2
				jugando=0
			#Conexion vertical
			if A[i][j]==A[i+1][j]==A[i+2][j]==A[i+3][j]==1:
				winner=1
				jugando=0
			elif A[i][j]==A[i+1][j]==A[i+2][j]==A[i+3][j]==2:
				winner=2
				jugando=0
	return winner,jugando