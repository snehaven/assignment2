
import math
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
	encrypted = "" #empty string for encrypted message
	n = len(strng) #take length of string input

	#assign rows and coloumns to matrix
	if (n%4==0):
		rows, cols = (int(n/4), 4)
	else:
		rows, cols = (int(n/4)+1, 4)
	#create empty matrix
	mat = [["*" for i in range(cols)] for j in range(rows)]

	#populate unencrpted matrix
	pos = 0
	for i in range(rows):
		for j in range(4):
			if(pos<len(strng)):
				mat[i][j] = strng[pos]
				pos += 1
			else:
				mat[i][j] = "*"

	#create encrpted message
	for i in range(4):
		for j in range(rows-1, -1, -1):
			if(mat[j][i] == "*"):
				continue
			else:
				encrypted += mat[j][i]

	return encrypted

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
	
	# calculate the dimension of the matrix
	 if math.sqrt( len( strng ) ) == int ( math.sqrt( len( strng ) ) ):
                n = int ( math.sqrt( len( strng ) ) )
        else:
                n = int( math.sqrt( len( strng ) ) ) + 1
        new_strng = strng

	# create an empty matrix
        decrypted = []
        for i in range ( n ):
                row = []
                for j in range ( n ):
                        row.append( " " )
                decrypted.append( row )

        for num in range ( n ** 2 - int( len( strng ) ) ):
                new_strng += "*"
	
	# fill in the matrix with the asterisks
        num = 1
        
        for y in range ( n ):
                x = n - 1
                while x >= 0:
                        if num <= ( n ** 2 - int( len( strng ) ) ):
                                decrypted[x][y] = "*"
                                num += 1
                        else:
                                break
                        x -= 1
        character = 0
	
	
        # fill in the rest of the matrix with the messenge
        for a in range ( len(decrypted) ):
                for b in range ( len(decrypted[a]) ):
                        if decrypted[a][b] != "*":
                                decrypted[a][b] = new_strng[ character ]
                                character += 1
	
	# decrypt the messenge into a string
        result = ""
        d = n - 1
        while d >= 0:
                for c in range ( n ):
                        if decrypted[c][d] != "*":
                                result += decrypted[c][d]
                d -= 1

        return result

def main():
	import sys
	# read the strings P and Q from standard input
	P = sys.stdin.readline()
        Q = sys.stdin.readline()
	
	# encrypt the string P
	encrypted = encrypt ( P )
	
	# decrypt the string Q
	decrypted = decrypt ( Q )

	# print the encrypted string of P
	print ( encrypted )
	
	# and the decrypted string of Q
	print ( decrypted )

if __name__ == "__main__":
  main()


