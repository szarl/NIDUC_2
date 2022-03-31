import random

def losoweBajty(ile):
    out= [0]*ile
    for i in range(ile):
        out[i] = random.sample(range(256), counts=[1]*256,k=1)[0]
    return out


def losoweBity(ile,przewagazer=1):
    out= [0]*ile
    for i in range(ile):
        out[i] = random.sample([0, 1], counts=[przewagazer, 1],k=1)[0]
    return out

if __name__ == '__main__':
    print(losoweBajty(24));
    print(losoweBity(24));
    print(losoweBity(24,9));#90% to zera