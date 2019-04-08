#!/usr/bin/python
import os
import sys
import string



class PasswordCheck():

    rule_dict = {'exist_case' : 0, 'cases' : 0, 'number_case' : 0, 'spl_char_case' : 0, 'len_case' : 0}
    pass_list= []
    pass_rev_list = []
    path = os.path.abspath('mydict.txt')
    with open(path, 'r') as f:
        str = f.readlines()
        for line in str:
            pass_list.append(line.strip())
            pass_rev_list.append(line.strip()[::-1])
    
    def __init__(self, password):
        self.password = password
        self.invalid_flag = 0
        self.length_flag = 1
        self.checkLength(password)
        if PasswordCheck.rule_dict['len_case'] is not 1:
            print("Password Length is less than 8 characters... Try again later!")
            
        else:
            self.length_flag = 0
            
    def checkLength(self, password):
        if len(password) >= 8:
            PasswordCheck.rule_dict['len_case'] = 1    
    
    
    def checkDict(self, password):
        if password in PasswordCheck.pass_list:
            print("INVALID PASSWORD. Can't use your old password. Try again with a new password.")
            self.invalid_flag = 1
        elif password in PasswordCheck.pass_rev_list:
            print("INVALID PASSWORD. Can't use another version of your old Password. Try again with a brand new password.")
            self.invalid_flag =1
        else:
            PasswordCheck.rule_dict['exist_case'] = 1    
    
    
    def checkLetterCases(self, password):
        count_dict = {'l': 0, 'u' : 0}
        for letter in password:
            if count_dict['l'] < 1:        
                if letter.islower():
                    count_dict['l'] = 1
            if count_dict['u'] < 1:
                if letter.isupper():
                    count_dict['u'] = 1
                
            if count_dict['l'] == 1 and count_dict['u'] == 1:
                PasswordCheck.rule_dict['cases'] = 1
                return 0
        if count_dict['l'] == 0:        
            print("The password does not have at least one LOWER CASE letter. Try with different password")
        if count_dict['u'] == 0:
            print("The password does not have at least one UPPER CASE letter. Try with different password")
         
        return 1
    
    def checkNumber(self, password):
        for letter in password:
            if letter.isdigit():
                PasswordCheck.rule_dict['number_case'] = 1
                break
    
    def checkSpecialChars(self, password):
        for letter in password:
            if letter in string.punctuation:
                PasswordCheck.rule_dict['spl_char_case'] = 1
                break
        
            
def main():

    strength = ''
    password = raw_input("Enter your desired password: ")
    pc = PasswordCheck(password)
    if pc.length_flag == 1:
        print("Password INVALID")
        sys.exit(1)
    strength = 'Weak'        
    pc.checkDict(password)
    if pc.invalid_flag == 1:
        print("Password Strength: INVALID")
        sys.exit(1)    
    letter_ret = pc.checkLetterCases(password)
    pc.checkNumber(password)
    pc.checkSpecialChars(password)
    passed = [x for x in pc.rule_dict.values() if x==1]
    if len(passed) >= 4:
        strength = 'Strong'
    elif len(passed) == 3:
        strength = 'Medium'

    print("Your Password Strength as per our analysis: '" + str(strength).upper() + "'")        
    
    return 0    
   


if __name__ == "__main__":
    main()
    
    
