
import math
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
	pass

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
	 if math.sqrt( len( strng ) ) == int ( math.sqrt( len( strng ) ) ):
                n = int ( math.sqrt( len( strng ) ) )
        else:
                n = int( math.sqrt( len( strng ) ) ) + 1
        new_strng = strng

        decrypted = []
        for i in range ( n ):
                row = []
                for j in range ( n ):
                        row.append( " " )
                decrypted.append( row )

        for num in range ( n ** 2 - int( len( strng ) ) ):
                new_strng += "*"

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
        
        for a in range ( len(decrypted) ):
                for b in range ( len(decrypted[a]) ):
                        if decrypted[a][b] != "*":
                                decrypted[a][b] = new_strng[ character ]
                                character += 1

        result = ""
        d = n - 1
        while d >= 0:
                for c in range ( n ):
                        if decrypted[c][d] != "*":
                                result += decrypted[c][d]
                d -= 1

        return result

def main():
  # read the strings P and Q from standard input
	P = input()
        Q = input()

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


