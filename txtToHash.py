from hashlib import md5

def encoder(phrase):
    return (md5(phrase.encode())).hexdigest()

def prehash(fileOrigin, prehashFile):
    f = open(f'{fileOrigin}', 'r')
    passwds = (f.read()).split('\n')
    hashed = open(f'{prehashFile}', 'a')
    check = open(f'{prehashFile}', 'r')
    if len(check.read()) == 0:
        for i in passwds:
            results = encoder(i)
            results = results + '\n'
            hashed.write(results)
    f.close()
    hashed.close()
    check.close()

