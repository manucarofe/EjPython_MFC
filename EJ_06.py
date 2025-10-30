# Calcular descuento

print("Escribe el precio original del producto: ")
precioOriginal = input()
print("Escribe el precio de venta del producto: ")
precioVenta = input()
descuentoAbsoluto = precioOriginal - precioVenta
if precioOriginal > 0:
    porcentajeDescuento = (descuentoAbsoluto / precioOriginal) * 100
print("El porcentaje de descuento es: ", porcentajeDescuento, "%")
