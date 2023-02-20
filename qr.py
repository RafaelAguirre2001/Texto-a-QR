import qrcode

# Texto que se convertirá en código QR
texto = "¡Hola, Mundo!"

# Crear un objeto QRCode
codigo_qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Agregar datos al objeto QRCode
codigo_qr.add_data(texto)
codigo_qr.make(fit=True)

# Crear imagen QRCode
imagen_qr = codigo_qr.make_image(fill_color="black", back_color="white")

# Guardar imagen QRCode
nombre_archivo = "qr.png"
imagen_qr.save(nombre_archivo)
