import re
def check_splcharacter(test):
   string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

   if (string_check.search(test) == None):
        print("String does not contain Special Characters.")
   else:
      print("String contains Special Characters.")
if __name__ == '__main__':
    # Enter the string to be checked

    test = "Code%Speedy"

    # calling check_splcharacter function

    check_splcharacter(test)