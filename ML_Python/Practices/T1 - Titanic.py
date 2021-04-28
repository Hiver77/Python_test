import pandas as pd

path = "../datasets/titanic/titanic3.csv"
df = pd.read_csv(path)
mainpath = "../datasets/"
# read.csv(filepath=path,
#          sep=",",
#          dtype={"ingresos": np.float64, "edad": np.int32},
#          header=0, names={"ingresos", "edad"},
#          skiprows=12, index_col=None,
#          skip_blank_lines=False, na_filter=False
#          )

# data3 = open(mainpath + "/" + "customer-churn-model/Customer Churn Model.txt", 'r')
# cols = data3.readline().strip().split(",")
# n_cols = len(cols)
#
# counter = 0
# main_dict = {}
# for col in cols:
#     main_dict[col] = []
#
#
# for line in data3:
#     values = line.strip().split(",")
#     for i in range(len(cols)):
#         main_dict[cols[i]].append(values[i])
#     counter += 1
#
# print("El data set tiene %d filas y %d columnas"%(counter-1, n_cols))

infile = mainpath + "/" + "customer-churn-model/Customer Churn Model.txt"
outfile = mainpath + "/" + "customer-churn-model/Table Customer Churn Model.txt"

with open(infile, "r") as infile1: #abre un archivo y se asigna un alias -> as Name
    with open(outfile, "w") as outfile1:
        for line in infile1:
            fields = line.strip().split(",")
            outfile1.write("\t".join(fields))
            outfile1.write("\n")


df4 = pd.read_csv(outfile, sep = "\t")
print(df4.head())


medals_url = "http://winterolympicsmedals.com/medals.csv"
medals_data = pd.read_csv(medals_url)
print(medals_data.head())


import dask
