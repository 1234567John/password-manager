import os   
file_path='passwords.txt' #file = passwords.txt
charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, " 

#Defining Encryption and Decryption
def encrypt(clearText):
 return''.join([charSet[(charSet.find(c)+3)%95] for c in clearText])    
def decrypt(decText):
 return''.join([charSet[(charSet.find(c)-3)%95] for c in decText])  

if not os.path.exists(file_path): #Checks to see if the file called "passwords.txt" is created and if not, it will create one   
    with open(file_path, 'w') as file:  
        file.write("") 

print('Welcome to Apps2U Password Manager! Enter any of the options in the square brackets:')   
choice='' #This defines choice as a variable 
while choice !='q':   

#The available options to choose from \n = new line
    print('[1] Add credentials')    
    print('\n[2] Check your stored credentials')   
    print('\n[q] Exit password manager\n')   
    choice=input() #This prompts the user their input  

    if choice=='1':     
          #Gives the user to input their credentials in, which is added to the file/list of credentials and is encrypted 
        with open(file_path, 'a')as file:  
         username=input('Enter your username:')
         encrypted_username=encrypt(username)
         file.write(encrypted_username+'\n')  
         print('\nUsername has been added')

         password=input('\nEnter your password:') 
         encrypted_password=encrypt(password)
         file.write(encrypted_password+'\n')
         print('\nPassword has been added:')

         urlresource=input('\nEnter your URL/resource:')
         encrypted_urlresource=encrypt(urlresource)
         file.write(encrypted_urlresource+'\n')
         print('\nURL/resource has been added:')

    elif choice=='2':  
     print('\nList of credentials:')   
     print('Username/Password/URLresource\n')
     with open(file_path,'r') as file:  #reads the file
      lines=file.readlines()
      credentials=[line.strip()for line in lines]#removes the /n at the end of each credential
      decryption=[decrypt(c)for c in credentials]#decrypts the credentials that happened in option 1,
      print(f"[{', '.join(decryption)}]\n")  #the credentials are printed in this format []

    elif choice=='q':   
        print('\nExiting Password Manager')   
        break  #This will close the program  

    else:   
        print('Invalid option, please try again')  #If the user types anything that isn't listed in the options, this will output  
print('Thanks for using Apps2U Password Manager!') #Goodbye message  


 


    

