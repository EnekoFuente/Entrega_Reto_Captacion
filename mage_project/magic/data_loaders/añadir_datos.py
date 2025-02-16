from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from os import path

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_postgres(data, *args, **kwargs):
    """
    Carga los datos en la tabla ventas_transformado en PostgreSQL.
    Si los datos ya existen, los reemplaza.
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        # Insertar los datos en la tabla ventas_transformado, manejando duplicados
        loader.export(
            df=data,  # Asegurar que se pasa el DataFrame
            table_name='ventas_transformado',  # Nombre de la tabla en PostgreSQL
            if_exists='replace',  # Reemplazar los datos existentes
            index=False  # No agregar el índice del DataFrame como columna
        )

    return data  # Devuelve los datos insertados


@test
def test_output(output, *args) -> None:
    """
    Verifica que los datos hayan sido insertados correctamente.
    """
    assert output is not None, 'El resultado está vacío'
    assert len(output) > 0, 'No se insertaron datos en ventas_transformado'
