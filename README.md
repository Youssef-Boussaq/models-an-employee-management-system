IR: This class represents the income tax rate (IR) with different tranches and rates. It has a static method getIR(salaire) to get the tax rate based on the salary.

IEmploye: This is an abstract base class (ABC) that defines the interface for an employee. It declares three abstract methods: age(), anciennete(), and dateRetraite(ageRetraite).

Employe: This class implements the IEmploye interface and adds some common attributes and methods for an employee, such as nom (name), dateNaissance (birth date), dateEmbauche (hiring date), and salaireBase (base salary). It also declares an abstract method salaireAPayer().

Formateur and Agent: These are subclasses of Employe that represent different types of employees. They provide their own implementations of the salaireAPayer() method.
