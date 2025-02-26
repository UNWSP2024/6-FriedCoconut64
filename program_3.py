
def sales_calc(sales):
    state = sales * .05
    county = sales * .025
    total = county + state
    return state, county, total

def main():
    sales = float(input("Type total monthly sales: "))
    state, county, total = sales_calc(sales)
    print("State sales tax is:", state)
    print("County sales tax is:", county)
    print("Total sales tax is:", total)

main()

# Program #3, Donovan Thompson 2/26/2025
