import pulp

beverage = pulp.LpProblem("Producing drinks", pulp.LpMaximize)  # Максимізація

lemonade = pulp.LpVariable("lemonade", lowBound=0, upBound=30, cat=pulp.LpInteger)
juice = pulp.LpVariable("juice", lowBound=0, upBound=20, cat=pulp.LpInteger)

beverage += lemonade + juice, "Max_quantity"

beverage += 2 * lemonade + juice <= 100, "Water"

beverage.solve()
print(f"Status: {pulp.LpStatus[beverage.status]}")
print(f"lemonade = {pulp.value(lemonade)}")
print(f"juice = {pulp.value(juice)}")