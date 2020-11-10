import string


class Password:
    def __init__(self):
        self.special_characters = set(string.punctuation.replace("_", ""))

    def ValidPassword(self, password):
        if not isinstance(password, str):
            raise TypeError("Password is not of type string!")

        if len(password) >= 8:
            if any(x.isupper() for x in password) and any(x.isdigit() for x in password) and any(
                    x in self.special_characters for x in password):
                return True
            else:
                return False
        else:
            return False

    def ValidPasswordWithDocTest(self, password):
        """
        Takes string and returns True if string is valid or False if it is not
        >>> ps = Password()
        >>> ps.ValidPasswordWithDocTest("")
        False
        >>> ps.ValidPasswordWithDocTest("AaBbCc123#")
        True
        >>> ps.ValidPasswordWithDocTest("ABc12#")
        False
        >>> ps.ValidPasswordWithDocTest("aabbcc123#")
        False
        >>> ps.ValidPasswordWithDocTest("AaBbCc#&$")
        False
        >>> ps.ValidPasswordWithDocTest("AaBbCc123")
        False
        >>> ps.ValidPasswordWithDocTest(2115)
        Traceback (most recent call last):
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad2.py", line 55, in <module>
            ps.ValidPasswordWithDocTest(2115)
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad2.py", line 39, in ValidPasswordWithDocTest
            raise TypeError("Password is not of type string!")
        TypeError: Password is not of type string!
        >>> ps.ValidPasswordWithDocTest([])
        Traceback (most recent call last):
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad2.py", line 62, in <module>
            ps.ValidPasswordWithDocTest([])
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad2.py", line 46, in ValidPasswordWithDocTest
            raise TypeError("Password is not of type string!")
        TypeError: Password is not of type string!
        """
        if not isinstance(password, str):
            raise TypeError("Password is not of type string!")

        if len(password) >= 8:
            if any(x.isupper() for x in password) and any(x.isdigit() for x in password) and any(
                    x in self.special_characters for x in password):
                return True
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'ps': Password()})
