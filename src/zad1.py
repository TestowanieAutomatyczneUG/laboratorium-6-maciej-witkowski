class Hamming:
    def distance(self, a, b):
        if len(a) == len(b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count
        else:
            raise ValueError("Invalid length of a string or b string")

    def distanceWithDocTest(self, a, b):
        """
        Takes two strings and returns how many chars are not the same
        >>> hamming = Hamming()
        >>> hamming.distanceWithDocTest("", "")
        0
        >>> hamming.distanceWithDocTest("A", "A")
        0
        >>> hamming.distanceWithDocTest("G", "T")
        1
        >>> hamming.distanceWithDocTest("GGACGGATTCTG", "AGGACGGATTCT")
        9
        >>> hamming.distanceWithDocTest("GGACTGAAATCTG", "GGACTGAAATCTG")
        0
        >>> hamming.distanceWithDocTest("AATG", "AAA")
        Traceback (most recent call last):
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad1.py", line 45, in <module>
            hamming.distanceWithDocTest("AATG", "AAA")
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad1.py", line 38, in distanceWithDocTest
            raise ValueError("Invalid length of a string or b string")
        ValueError: Invalid length of a string or b string
        >>> hamming.distanceWithDocTest("ATA", "AGTG")
        Traceback (most recent call last):
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad1.py", line 48, in <module>
            hamming.distanceWithDocTest("ATA", "AGTG")
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad1.py", line 41, in distanceWithDocTest
            raise ValueError("Invalid length of a string or b string")
        ValueError: Invalid length of a string or b string
        >>> hamming.distanceWithDocTest("", "G")
        Traceback (most recent call last):
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad1.py", line 55, in <module>
            (hamming.distanceWithDocTest("", "G")
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad1.py", line 48, in distanceWithDocTest
            raise ValueError("Invalid length of a string or b string")
        ValueError: Invalid length of a string or b string
        >>> hamming.distanceWithDocTest("G", "")
        Traceback (most recent call last):
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad1.py", line 62, in <module>
            hamming.distanceWithDocTest("G", "")
          File "C:/Users/macie/OneDrive/Pulpit/STUDIA/2 ROK/SEMESTR 1/Testowanie automatyczne/Laboratoria/Laboratorium - 10.11/src/zad1.py", line 55, in distanceWithDocTest
            raise ValueError("Invalid length of a string or b string")
        ValueError: Invalid length of a string or b string
        """
        if len(a) == len(b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count
        else:
            raise ValueError("Invalid length of a string or b string")


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'hamming': Hamming()})
