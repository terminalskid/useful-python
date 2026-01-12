# Currency Scan

pesos = int(input("How many pesos? "))
soles = int(input("How many soles? "))
reais = int(input("How many reais? "))

# Exchange rates

exr = 0.1842 # Reias
exp = 0.06 # Pesos
exs = 0.29 # Soles

# Calc Function

total = round(reais * exr + soles * exs + exp * pesos, 2)
print(f"You have: {total} USD")

# input = a question
# everything with = is a variable that stores info, neither are built in functions.
# print is the othing that writes in command line eg 'print("helloworld') is gonna say helloworld
# since we assigned all values and the math in total we can print either how much you have like i did or just the total with print(total) we have no " because it is a variable not a string.
