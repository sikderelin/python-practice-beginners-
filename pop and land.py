def main():
    population = float(input("enter the population number: "))
    land_area = float(input("enter the land_area number: "))
    density = population / land_area
    
    if population < 10000000:
        print(population)

    elif population in range(10000000 , 35000000 + 1):
            print(population)

    if density > 100:
        print("Densely Population")

    elif density < 100:
           print("Sparsely Population")

main()

    
    
