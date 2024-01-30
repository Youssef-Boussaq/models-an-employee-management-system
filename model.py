from abc import ABC, abstractmethod
from datetime import datetime

class IR(ABC):
    tranches = [0, 30001, 50001, 60001, 80001, 180001]
    tauxIR = [0, 0.1, 0.2, 0.3, 0.34, 0.38]

    @staticmethod
    def getIR(salaire):
        for i in range(len(IR.tranches)):
            if salaire < IR.tranches[i]:
                return IR.tauxIR[i-1]
        return IR.tauxIR[-1]

class IEmploye(ABC):
    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def anciennete(self):
        pass

    @abstractmethod
    def dateRetraite(self, ageRetraite):
        pass

class Employe(IEmploye):
    mtle = 0

    def _init_(self, nom, dateNaissance, dateEmbauche, salaireBase):
        self.mtle = Employe.mtle + 1
        self.nom = nom
        self.dateNaissance = dateNaissance
        self.dateEmbauche = dateEmbauche
        self.salaireBase = salaireBase

    def age(self):
        return datetime.now().year - self.dateNaissance.year

    def anciennete(self):
        return datetime.now().year - self.dateEmbauche.year

    def dateRetraite(self, ageRetraite):
        return self.dateNaissance.year + ageRetraite

    @abstractmethod
    def salaireAPayer(self):
        pass

    def _str_(self):
        return f"{self.mtle} - {self.nom} - {self.dateNaissance} - {self.dateEmbauche} - {self.salaireBase}"

    def _eq_(self, other):
        if isinstance(other, Employe):
            return self.mtle == other.mtle
        return False

class Formateur(Employe):
    tarifHsup = 70

    def _init_(self, nom, dateNaissance, dateEmbauche, salaireBase, heureSup):
        super()._init_(nom, dateNaissance, dateEmbauche, salaireBase)
        self.heureSup = heureSup

    def salaireAPayer(self):
        salaireBrut = self.salaireBase + self.heureSup * Formateur.tarifHsup
        return salaireBrut * (1 - IR.getIR(salaireBrut))

    def _str_(self):
        return super()._str_() + f" - {self.heureSup}"

class Agent(Employe):
    def _init_(self, nom, dateNaissance, dateEmbauche, salaireBase, primeResponsabilite):
        super()._init_(nom, dateNaissance, dateEmbauche, salaireBase)
        self.primeResponsabilite = primeResponsabilite

    def salaireAPayer(self):
        salaireBrut = self.salaireBase + self.primeResponsabilite
        return salaireBrut * (1 - IR.getIR(salaireBrut))

    def _str_(self):
        return super()._str_() + f" - {self.primeResponsabilite}"
