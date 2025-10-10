file to datafram
==> titanic = pd.read_csv("data/titanic.csv")

datafram to file 
==> titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)