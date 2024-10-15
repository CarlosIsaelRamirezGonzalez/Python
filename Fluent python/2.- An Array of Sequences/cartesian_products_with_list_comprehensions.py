colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors 
                         for size in sizes]
print(tshirts)

# Es lo mismo que :
for color in colors:
    for size in sizes:
        print((color, size))