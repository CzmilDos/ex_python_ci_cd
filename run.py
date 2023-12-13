"""
CI/CD
"""
import pandas as pd


def main():
    """
    Main
    """
    data = import_data()
    data = rename_columns(data)
    data_sample = sample_data(data)
    multiply_dataset(data_sample)
    data = create_total_sepal_column(data)
    data = create_total_petal_column(data)

    print("Shape du DataFrame : ", data.shape)

    print("Les deux premières lignes du DataFrame : ")
    print(data.head(2))


def import_data():
    """
    Import csv file as a dataframe
    Output: data [pd.DataFrame]
    """
    data = pd.read_csv("data/iris.csv")
    print(data.shape)
    return data


def rename_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Rename dataframe columns
    """
    data_renamed = data.rename(columns={"sepal.length": 'sepal_length',
        "sepal.width": 'sepal_width',
        "petal.length": 'petal_length',
        "petal.width": 'petal_width'}
                              )
    return data_renamed


def sample_data(data: pd.DataFrame, sample_size: int = 50) -> pd.DataFrame:
    """
    Create a sample of the DataFrame with a specified number of rows.

    Parameters:
    - data (pd.DataFrame): The input DataFrame.
    - sample_size (int): The number of rows to include in the sample. Default is 50.

    Returns:
    - sampled_data (pd.DataFrame): The DataFrame containing the sampled data.
    """
    sampled_data = data.sample(n=sample_size, random_state=42)  # random_state fixe pour assurer la reproductibilité des résult
    return sampled_data


def multiply_dataset(data: pd.DataFrame, multiplier: int = 3) -> pd.DataFrame:
    """
    Multiply the dataset by a specified factor using pd.concat.

    Parameters:
    - data (pd.DataFrame): The input DataFrame.
    - multiplier (int): The factor by which to multiply the dataset. Default is 3.

    Returns:
    - multiplied_data (pd.DataFrame): The DataFrame containing the multiplied data.
    """
    # Utilise pd.concat pour concaténer le DataFrame original plusieurs fois
    multiplied_data = pd.concat([data] * multiplier, ignore_index=True)
    return multiplied_data


def create_total_sepal_column(data: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new column "total_sepal" in the DataFrame as the sum of "sepal_length" and "sepal_width".

    Parameters:
    - data (pd.DataFrame): The input DataFrame.

    Returns:
    - data_with_total_sepal (pd.DataFrame): The DataFrame with the new "total_sepal" column.
    """
    # Ajoute une nouvelle colonne "total_sepal" en faisant la somme de "sepal_length" et "sepal_width"
    data_with_total_sepal = data.assign(total_sepal=data['sepal_length'] + data['sepal_width'])
    return data_with_total_sepal


def create_total_petal_column(data: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new column "total_petal" in the DataFrame as the sum of "petal_length" and "petal_width".

    Parameters:
    - data (pd.DataFrame): The input DataFrame.

    Returns:
    - data_with_total_petal (pd.DataFrame): The DataFrame with the new "total_petal" column.
    """
    # Ajoute une nouvelle colonne "total_petal" en faisant la somme de "petal_length" et "petal_width"
    data_with_total_petal = data.assign(total_petal=data['petal_length'] + data['petal_width'])
    return data_with_total_petal


if __name__ == '__main__':
    """
    Doc
    """
    main()
