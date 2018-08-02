
x = dict(a=1, b=2)
y = dict(a=2, b=2)

for x_values, y_values in zip(x.items(), y.items()):
    if x_values == y_values:
        print( 'ok' , x_values, y_values)
    else:
        print("not", x_values, y_values)