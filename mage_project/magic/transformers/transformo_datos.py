if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    """
    Transformación de datos:
    1. Convertir los nombres de los productos a minúsculas.
    2. Aplicar un descuento del 10% al precio de los productos.
    """
    # Convertir los nombres de los productos a minúsculas
    if 'producto' in data.columns:
        data['producto'] = data['producto'].str.lower()

    # Aplicar un descuento del 10% al precio de los productos
    if 'precio' in data.columns:
        data['precio'] = data['precio'] * 0.9  # 10% de descuento

    return data


@test
def test_output(output, *args) -> None:
    """
    Verificar que los datos transformados sean correctos.
    """
    assert output is not None, 'The output is undefined'

    # Asegurarse de que los nombres de los productos estén en minúsculas
    assert output['producto'].str.islower().all(), "No todos los nombres de productos están en minúsculas"

     # Restaurar el precio original para la validación
    precio_original = output['precio'] / 0.9

    # Verificar que el descuento del 10% se aplicó correctamente
    assert (precio_original * 0.9 == output['precio']).all(), "El descuento no se aplicó correctamente"