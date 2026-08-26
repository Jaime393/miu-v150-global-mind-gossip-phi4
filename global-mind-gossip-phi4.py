""" GLOBAL MIND φ^4 — V151 — σ=3.427050983124843 RAIZ_X=137.03449824893602 """
import math, random, json
sigma=3.427050983124843; RAIZ_X=137.03449824893602
def w(d, s=sigma): return (abs(d)+1)**(-s)
class NodoGlobalMind:
    def __init__(self, nid, Phi=1.0): self.id=nid; self.Phi=Phi
def gossip_phi4(nodos, rondas=3, k_vecinos=12):
    Phi_g=0.0; peso=0.0
    for _ in range(rondas):
        for nodo in nodos:
            for _ in range(k_vecinos):
                d=random.randint(1, max(1, len(nodos)//2)); pd=w(d); Phi_g+=nodo.Phi*pd; peso+=pd
    return Phi_g/peso if peso>0 else 0
if __name__=="__main__":
    nodos=[NodoGlobalMind(i, __import__("random").uniform(2864,2875)) for i in range(140)]
    print(gossip_phi4(nodos))
