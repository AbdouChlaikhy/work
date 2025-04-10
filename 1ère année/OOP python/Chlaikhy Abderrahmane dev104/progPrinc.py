

from appareil import Appareil
from veloElec import VeloElec


if __name__=='__main__':
    try:
        ap1=Appareil("AA/667",400,2,3000)
        print(ap1)
        ap1.ClassEneergetique()
        vel1=VeloElec("AB/523",700,5.2,5500,4,500)
        print(vel1)
        vel1.Charger(40)
        print(vel1)
         
    except Exception:
         
        print("Invalid Reference")     

