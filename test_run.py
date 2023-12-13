"""
Tests
"""
from run import import_data
from run import rename_columns
from run import sample_data
from run import multiply_dataset
from run import create_total_sepal_column
from run import create_total_petal_column
import numpy as np
import pandas as pd


def test_import_data():
    """
    Test
    """
    data = import_data()
    assert data.shape[0] > 0


def test_rename_columns():
    """
    Doc
    """
    data = import_data()
    data_renamed = rename_columns(data)
    assert "sepal_length" in data_renamed.columns


def test_sample_data():
    # Crée un DataFrame de test avec 100 lignes
    test_data = pd.DataFrame({
        'A': np.arange(1, 101),
        'B': np.random.rand(100)
    })

    # Appelle la fonction sample_data pour obtenir un échantillon
    sampled_data = sample_data(test_data, sample_size=50)

    # Vérifie que le résultat est bien un DataFrame
    assert isinstance(sampled_data, pd.DataFrame), "Le résultat n'est pas un DataFrame."

    # Vérifie que le nombre de lignes dans l'échantillon est égal à sample_size
    assert len(sampled_data) == 50, f"La taille de l'échantillon devrait être de 50, mais elle est de {len(sampled_data)}."


def test_multiply_dataset():
    # Crée un DataFrame de test avec 50 lignes
    test_data = pd.DataFrame({
        'A': np.arange(1, 51),
        'B': np.random.rand(50)
    })

    # Appelle la fonction multiply_dataset pour obtenir un DataFrame multiplié
    multiplied_data = multiply_dataset(test_data, multiplier=3)

    # Vérifie que le résultat est bien un DataFrame
    assert isinstance(multiplied_data, pd.DataFrame), "Le résultat n'est pas un DataFrame."

    # Vérifie que le nombre de lignes dans le DataFrame multiplié est correct
    expected_rows = len(test_data) * 3
    assert len(multiplied_data) == expected_rows, f"taille expérée: {expected_rows}, obtenue: {len(multiplied_data)}."


def test_create_total_sepal_column():
    # Crée un DataFrame de test avec 50 lignes
    test_data = pd.DataFrame({
        'sepal_length': np.random.rand(50),
        'sepal_width': np.random.rand(50)
    })

    # Appelle la fonction create_total_sepal_column pour obtenir un DataFrame avec la nouvelle colonne
    data_with_total_sepal = create_total_sepal_column(test_data)

    # Vérifie que le résultat est bien un DataFrame
    assert isinstance(data_with_total_sepal, pd.DataFrame), "Le résultat n'est pas un DataFrame."

    # Vérifie que la colonne "total_sepal" a été ajoutée
    assert 'total_sepal' in data_with_total_sepal.columns, "La colonne 'total_sepal' n'a pas été ajoutée."

    # Vérifie que les valeurs dans la colonne "total_sepal" sont correctes
    expected_values = test_data['sepal_length'] + test_data['sepal_width']
    assert data_with_total_sepal['total_sepal'].equals(expected_values), "Valeurs de 'total_sepal' non correctes."


def test_create_total_petal_column():
    # Crée un DataFrame de test avec 50 lignes
    test_data = pd.DataFrame({
        'petal_length': np.random.rand(50),
        'petal_width': np.random.rand(50)
    })

    # Appelle la fonction create_total_petal_column pour obtenir un DataFrame avec la nouvelle colonne
    data_with_total_petal = create_total_petal_column(test_data)

    # Vérifie que le résultat est bien un DataFrame
    assert isinstance(data_with_total_petal, pd.DataFrame), "Le résultat n'est pas un DataFrame."

    # Vérifie que la colonne "total_petal" a été ajoutée
    assert 'total_petal' in data_with_total_petal.columns, "La colonne 'total_petal' n'a pas été ajoutée."

    # Vérifie que les valeurs dans la colonne "total_petal" sont correctes
    expected_values = test_data['petal_length'] + test_data['petal_width']
    assert data_with_total_petal['total_petal'].equals(expected_values), "Valeurs de 'total_petal' non correctes."
