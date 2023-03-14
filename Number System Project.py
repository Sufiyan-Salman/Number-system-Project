#Project for ics first semester Morning SE
#Sufiyan Mohammad Salman (B20103065)
#points conversion can also be performed here

#====================
#Func for value to dec
#====================
def ValuetoDecimal(d,base,Rvalue_Base,message):

        d=str(d)
        a=0
        c=0
        n=0 #power
        #to find lenght of binary before pooint value starts
        while(a<len(d)):
            
            if(d[a]=='.'):
                break
            #print(d[a])
            n+=1
            a+=1
        a=0
        while(a<len(d)):
            n-=1 # ye power k lie hai q k power ek kam se shuru hoti hai and 0 tk jati hai
            power_after_point=1  # ye power negativ powr k lie use hoga
            #point k baad k numbers klie
           
            m=1
         # ye below if ka jo block hai thats for point wali values
            if(d[a]=='.'):
                a+=1
                while(a<len(d)):
                    v=d[a]
                    if(base==16):
                        if(v=='A'):
                            v=10       
                            b=(base**(-power_after_point))*int(v)
                        elif(v=='B'):
                            v=11       
                            b=(base**(-power_after_point))*int(v)
                        elif(v=='C'):
                            v=12       
                            b=(base**(-power_after_point))*int(v)
                        elif(v=='D'):
                            v=13       
                            b=(base**(-power_after_point))*int(v)
                        elif(v=='E'):
                            v=14       
                            b=(base**(-power_after_point))*int(v)
                        elif(v=='F'):
                            v=15
                            b=(base**(-power_after_point))*int(v)
                        elif(int(v)>=0 and int(v)<=9):
                            b=(base**(-power_after_point))*int(v)
                        else:
                            print("Wrong Hexa input at index value",a,"which is '",d[a],"'")
                            m=0
                            break
                    elif(base==2):
                       if(int(v)==0 or int(v)==1):
                            b=(base**(-power_after_point))*int(v)
                       else:
                            print("Wrong binary input at index value",a,"which is '",d[a],"'")
                            m=0
                            break
                    elif(base==8):
                        if(int(v)>=0 and int(v)<=7):
                            b=(base**(-power_after_point))*int(v)
                        else:
                            print("Wrong octal input at index value",a,"which is '",d[a],"'")
                            m=0
                            break
                    power_after_point+=1
                    a+=1
                    c+=b                    
                    break
            #this block is for normal values
            else:                 
                 v=d[a]
                 if(base==16):
                    if(v=='A'):
                        v=10       
                        b=(base**n)*int(v)
                    elif(v=='B'):
                        v=11       
                        b=(base**n)*int(v)
                    elif(v=='C'):
                        v=12       
                        b=(base**n)*int(v)
                    elif(v=='D'):
                        v=13       
                        b=(base**n)*int(v)
                    elif(v=='E'):
                        v=14       
                        b=(base**n)*int(v)
                    elif(v=='F'):
                        v=15
                        b=(base**n)*int(v)
                        
                    elif(int(v)>=0 and int(v)<=9):
                            b=(base**n)*int(v)
                            

                    else:
                            print("Wrong Hexa input at index value",a,"which is '",d[a],"'")
                            m=0
                            break
                 elif(base==2):
                   if(int(v)==0 or int(v)==1):
                        b=(base**n)*int(v)
                        
                   else:
                        print("Wrong binary input at index value",a,"which is '",d[a],"'")
                        m=0
                        break
                 elif(base==8):
                    if(int(v)>=0 and int(v)<=7):
                        b=(base**n)*int(v)
                    else:
                        print("Wrong octal input at index value",a,"which is '",d[a],"'")
                        m=0
                        break
                 
                 c+=b
                 a+=1
        if(Rvalue_Base=='All'):
                print(message,'=',c)
        if(m==1):
            return(c)
'''
Rvalue_base islie dala hamne q k is function me hamne condition dali hai ke agar
ye rvalue_base 'All' k equal ho to sare required values print krde,ab wo All ki condition argument me se
hi check krlega
'''
#==========================================
#Func for Dec to required value
#==========================================
def DecimaltoValue(d,base,Rvalue_Base,message):
        b=''
        dec=str(d)
        a=0
        #to check if given value point me hai ya normal hai
        while(a<len(dec)):
            
            if(dec[a]=='.'):
                dec=float(dec)
                chk='Y'
                break
            #if(base==):
            b+=dec[a]
            chk='N'
            a+=1
        if(chk=='N'):
            dec=int(dec)
        pointValue=float(b)-dec #full value me se only point se pehle ka minus
        # 'b' hai point se pehle ki value
        # 'dec' hai point k baad ki value
        #for example 2.875 is 'dec' and is me 2 is 'b'  and .875 is 'pointValue'
        a=0
        #========

        while True:
                   carry=''
                   c=''
                   b=int(b) 
                   while(b/base!=0): 
                        a=b%base  # ye us number ka reminder nikalega to jo k right pe aata hai
                        b=int(b/base)# ye given number ko base se divide krta rahega
                        if(base==16):
                            if(a==10):   
                                a='A'
                            elif(a==11):
                                a='B'
                            elif(a==12):
                                a='C'
                            elif(a==13):
                                a='D'
                            elif(a==14):
                                a='E'
                            elif(a==15):
                                a='F'
                            c+=str(a)
                        else:
                            c+=str(a)
                   n=1   # agar list k zariye krte ham to bas reverse laga dete but due to string-
                   y=''  # -ye 5 lines likheen
                   while(n<=len(c)):
                        y+=c[-n]
                        n+=1
                   carry+=y
                   if(carry==''):
                       carry+='0'
                   if(chk=='Y'):
        #is if k andar point ke baad ki value jo ke dec hai wo process hogi
                       carry+='.' # take value jo hai uske baad point add hojaye 
                       v=0
                       if(pointValue<1):
                         pointValue=pointValue*(-1)
                       while True:
                            pointValue=pointValue*base  
                            
                            if(pointValue>1):
                                a=int(pointValue) # point se pehle zero se bara ajaye to wo sab variable a me store hoga
                                pointValue=pointValue-a   # taake value dubara 1 se less hojaye
                                if(base==16):
                                    if(a==10):   
                                        a='A'
                                    elif(a==11):
                                        a='B'
                                    elif(a==12):
                                        a='C'
                                    elif(a==13):
                                        a='D'
                                    elif(a==14):
                                        a='E'
                                    elif(a==15):
                                        a='F'
                                    carry+=str(a)
                                else:
                                    carry+=str(a) # ye wo value store krega jo point se pehle aae
                                
                            elif(pointValue==0.0):
                               v=10
                               break
                            elif(pointValue==1):
                               #print(pointValue)
                               carry+='1'  # ye condiitonn is lie k agar 1 ajaye to loop ruk jaye
                               v=10
                               break
                            else:
                               carry+='0'
                            if(v==10): # inner loop k lie
                                break
                            v+=1
                   else:
                     break
                   if(v==10):# outer loop k lie
                         break
        if(Rvalue_Base=='All'):
                        print(message,'=',carry)
        return (carry)
                

'''
Rvalue_base islie dala hamne q k is function me hamne condition dali hai ke agar
ye rvalue_base 'All' k equal ho to sare required values print krde,ab wo All ki condition argument me se
hi check krlega aur jo neeche itni saari lines hen sirf All wale ko print krne k liewo khatam kr sakenge ham.
Asal value jisme ye convert krega wo base argument me hai
'''





#================================================================#
#Function for arithmetic opertations
#================================================================#
def arithmetic_operations(first_value,second_value,base,operator,message):
#yahan neeche function me rvalue base argument is not needed but 0 take error na aye is needed to make answer print
#ham ye bhi krskte hen k function me rvalue base parameter ko default value assign krden , in this way ye zero nai lagana prega
        Decimal1=ValuetoDecimal(first_value,base,0,'Decimal')
        Decimal2=ValuetoDecimal(second_value,base,0,'Decimal')
        c=(Decimal1/Decimal2)
        if(operator=='/'):
            remainder=Decimal1%Decimal2
            if(remainder==0):
               c=Decimal1/Decimal2
               print(c)
            else:
               v=(Decimal1/Decimal2)
            message1=DecimaltoValue(c,base,0,message)# ye divide ka answer excluding remainder
            message2=DecimaltoValue(remainder,base,0,message)# ye remainder k lie
            print(d1,'/',d2,'=',message1 ,'and remainder =',message2)
        elif(operator=='+'):
            Decimal=Decimal1+Decimal2
            message1=DecimaltoValue(Decimal,base,0,message)
            print(d1,'+',d2,'=',message1)
        elif(operator=='*'):
            Decimal=Decimal1*Decimal2
            message1=DecimaltoValue(Decimal,base,0,message)
            print(d1,'*',d2,'=',message1)
        elif(operator=='-'):
            Decimal=Decimal1-Decimal2
            message1=DecimaltoValue(Decimal,base,0,message)
            print(d1,'-',d2,'=',message1)
#================================================================#
#Function for converting values to each other
#================================================================#
def converter(base,Rvalue_Base):
    #yahan rvalue base is needed mainly
    if(Rvalue_Base==base): #dusre value ki base=first value ki base
        print("Bases are same so answer would be same as given input")
       
    
    else:
        if(base==2):
            d=(input("Enter Binary value(1 or 0): "))
            Decimal=ValuetoDecimal(d,base,Rvalue_Base,'Decimal')
            Octal=DecimaltoValue(Decimal,8,Rvalue_Base,'Octal ')
            Hexadecimal=DecimaltoValue(Decimal,16,Rvalue_Base,'Hexadecimal')
            print("===============")

        elif(base==8):
            d=(input("Enter octal value(0-7): "))
            Decimal=ValuetoDecimal(d,base,Rvalue_Base,'Decimal')
            Binary=DecimaltoValue(Decimal,2,Rvalue_Base,'Binary')
            Hexadecimal=DecimaltoValue(Decimal,16,Rvalue_Base,'Hexadecimal')
            print("===============")
            
        elif(base==10):
            Decimal=(input("Enter Decimal value(0-9): "))
            Binary=DecimaltoValue(Decimal,2,Rvalue_Base,'Binary')
            Octal=DecimaltoValue(Decimal,8,Rvalue_Base, 'Octal ')
            Hexadecimal=DecimaltoValue(Decimal,16,Rvalue_Base,'Hexadecimal')
            print("===============")

        elif(base==16):
            print("==Enter Alphabet in capital letters==")
            d=(input("Enter Hexa value(0-9)(A-F): "))
            Decimal=ValuetoDecimal(d,base,Rvalue_Base,'Decimal')
            Octal=DecimaltoValue(Decimal,8,Rvalue_Base,'Octal')
            Binary=DecimaltoValue(Decimal,2,Rvalue_Base,'Binary')
            print("===============")
            '''
Rvalue_base islie dala hamne q k upr wale function me hamne condition dali hai ke agar
ye rvalue_base 'All' k equal ho to sare required values print krde,ab wo All ki condition argument me se
hi check krlega aur jo neeche itni saari lines hen sirf All wale ko print krne k liewo khatam kr sakenge ham.
            '''
            
    
    if(Rvalue_Base!=base):        
        if(Rvalue_Base==2):
            answer=Binary
            return(answer)
        elif(Rvalue_Base==8):
            answer=Octal
            return(answer)
        elif(Rvalue_Base==10):
            answer=Decimal
            return(answer)
        elif(Rvalue_Base==16):
            answer=Hexadecimal
            return(answer)


#===========================Main program========================#

q='y'
while(q!='n'):
        Input_Value=input("Enter value you want to work on(Dec,Hex,Bin,Oct) : ")
        if Input_Value in ['octal','o','O','Octal','OCTAL','oct','OCT','Oct']:
                  base=8
                  message='Octal'
                  print("      You chose Octal")
                  print("===============")
        elif Input_Value in ['decimal','d','D','DECIMAL','Decimal','dec','Dec','DEC']:
                  base=10
                  message='Decimal'
                  print("      You chose Decimal")
                  print("===============")
        elif Input_Value in ['hexa','HEXA','Hexa','hex','Hex','HEX','hexadecimal','h','H','HEXADECIMAL','Hexadecimal']:
                  base=16
                  message='Hexadecimal'
                  print("      You chose Hexadecimal")
                  print("===============")
        elif Input_Value in ['binary','b','B','Binary','BINARY','BIN','Bin','bin']:
                  base=2
                  message='Binary'
                  print("      You chose Binary")
                  print("===============")
        else:
            print("Try again,you typed wrong")
            print("===============")
            continue
            #break
#======================================  

        convert_or_arithmetic=input("Do you want to convert or want to perform arithmetic ops (c or a):")
        if convert_or_arithmetic in ['c','convert','C','Convert']:
                  print("      You chose conversion to be performed on the entered value")
                  print("===============")
                  convert_or_arithmetic='convert'
        elif convert_or_arithmetic in ['a','arithmetic','A','Arithmetic']:
                  print("      You chose arithmetic operations to be performed on the entered value")
                  print("===============")
                  convert_or_arithmetic='arithmetic operations'
        else:
            print("Try again,you typed wrong")
            print("===============")
            continue
            #break
#======================================  
            
        if(convert_or_arithmetic=='arithmetic operations'):
            print("M=Multiplication\nA=Addition\nD=Division\nS=Subtraction")
            print("===============")
            operator=input("Which operation you want to perform?(M,A,D,S): ")
            if operator in ['M','m','mul','Mul','Multiply','multiply']:
                  print("      You chose Multiplication")
                  print("===============")
                  operator='*'
            elif operator in ['A','a','add','Add','Addition','addition']:
                  print("      You chose Addition")
                  print("===============")
                  operator='+'
            elif operator in ['D','d','div','Div','Division','division']:
                  print("      You chose Division")
                  print("===============")
                  operator='/'
            elif operator in ['S','s','sub','Sub','Subtraction','subtraction']:
                  print("      You chose Subtraction")
                  print("===============")
                  operator='-'
            else:
                print("Try again,you typed wrong")
                print("===============")
                continue
                #break
            d1=input('Enter first value  :')
            d2=input('Enter second value :')
            print("===============")
            
            if(base==10):
                if(operator=='+'):
                    decimal=float(d1)+float(d2)
                    print(d1,'+',d2,'=',decimal)
                elif(operator=='-'):
                    decimal=float(d1)-float(d2)
                    print(d1,'-',d2,'=',decimal)
                elif(operator=='/'):
                    decimal=float(d1)/float(d2)
                    print(d1,'/',d2,'=',decimal)
                elif(operator=='*'):
                    decimal=float(d1)*float(d2)
                    print(d1,'*',d2,'=',decimal)
            else:
            
              arithmetic_operations(d1,d2,base,operator,message)
            print("===============")
#======================================  
            
        elif(convert_or_arithmetic=='convert'):
            Required_Value=input("Enter value in which answer should be given(Dec,Hex,Bin,Oct)or All :")
            if Required_Value in ['octal','o','O','Octal','OCTAL','oct','OCT','Oct']:
                      print("      Given value will be converted in octal      ") 
                      print("===============")
                      value='Octal'
                      message ='Octal'
                      Rvalue_Base=8
            elif Required_Value in ['decimal','d','D','DECIMAL','Decimal','dec','Dec','DEC']:
                      print("      Given value will be converted in decimal      ")
                      print("===============")
                      value='Decimal'
                      message='Decimal'
                      Rvalue_Base=10
            elif Required_Value in ['hexa','HEXA','Hexa','hex','Hex','HEX','hexadecimal','h','H','HEXADECIMAL','Hexadecimal']:
                      print("      Given value will be converted in hexadecimal      ")
                      print("===============")
                      value='Hexadecimal'
                      message='Hexadecimal'
                      Rvalue_Base=16
                      
            elif Required_Value in ['binary','b','B','Binary','BINARY','BIN','Bin','bin']:
                      print("      Given value will be converted in binary      ")
                      print("===============")
                      value='Binary'
                      message='Binary'
                      Rvalue_Base=2
            elif Required_Value in ['all','a','A','All','ALL']:
                      print("      Given value will be converted in all the other values")
                      print("===============")
                      value='All'
                      Rvalue_Base='All'
            else:
                print(" Try again,you typed wrong")
                continue
#======================================            
            if(value=='All'):
                converter(base,Rvalue_Base)
                
            else:
                answer=converter(base,Rvalue_Base)
                print(value,'=',answer)
                print("===============")
        q=input("Do you want to continue(y/n)?\n ")
        print("===============")
print('Thanks for using!')
#===================================
#Sir I have checked this program in the best way I could , Still if any problem persist please contact at : sufiyannsalmann@gmail.com
