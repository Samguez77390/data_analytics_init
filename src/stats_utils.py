import statistics
import pandas as pd
sales = pd.read_csv("data/sales.csv")
print(sales)
def analyser_ventes(transactions):
   
   # 1. Nettoyage des données
    valides = []
    for t in transactions:
       if t > 0:
           valides.append(t)

    nombre = len(valides)
    somme = sum(valides)
    moyenne = somme / nombre
    mediane = statistics.median(valides)
    ecart_type = statistics.pstdev(valides)

    maximum = max(valides)
    minimum = min(valides)

    seuil = 2 * moyenne

    anomalies = []
    for x in valides:
        if x > seuil:
            anomalies.append(x)
    print("voilà !")
    return {
        "nombre_transactions": nombre,
        "somme_totale": somme,
        "moyenne": moyenne,
        "mediane": mediane,
        "ecart_type": ecart_type,
        "maximum": maximum,
        "minimum": minimum,
        "seuil_anomalie": seuil,
        "anomalies": anomalies,
    }   
if __name__ == "__main__":
    ventes = [120, 85.5, -10, 0, 99, 150, 2000, 110, 95, 130, -5, 105]
    resultat = analyser_ventes(ventes)
    for cle, valeur in resultat.items():
        print(f"{cle} : {valeur}")



