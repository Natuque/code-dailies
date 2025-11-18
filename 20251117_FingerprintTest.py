** start of main.py **

def is_match(fingerprint_a, fingerprint_b):
    if fingerprint_a == fingerprint_b:
        print("True")
        return True
    
    elif len(fingerprint_a) == len(fingerprint_b):
        maxCount = len(fingerprint_a)
        count = 0
        differences = 0

        while count < maxCount:
            a = fingerprint_a[count]
            b = fingerprint_b[count]
            if a != b:
                differences += 1
                count += 1
            else:
                count += 1
        
        maxDiff = 0.10 * len(fingerprint_a)

        if differences <= maxDiff:
            print("True")
            return True
        else:
            print("False")
            return False

    else:
        print("False")
        return False
    

    return fingerprint_a


is_match("helloworld", "helloworld")
is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat")
is_match("helloworld", "helloworlds")

** end of main.py **

