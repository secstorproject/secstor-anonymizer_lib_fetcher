import time
from .settings import *
from threading import Semaphore
from concurrent.futures import ThreadPoolExecutor, wait
from .anonymizer.utils.data_processing import value_to_dataframe
from .anonymizer.lib.encryption import encrypt_aes, encrypt_chacha20, encrypt_salsa20
from .anonymizer.lib.generalization import age_generalization, percent_generalization
from .anonymizer.lib.hashing import apply_md5, apply_sha1, apply_sha256
from .anonymizer.lib.masking import mask_cpf, mask_email, mask_first_n_characters, mask_full, mask_last_n_characters, mask_range
from .anonymizer.lib.null_out import drop_columns
from .anonymizer.lib.perturbation import perturb_date, perturb_numeric_gaussian, perturb_numeric_laplacian, perturb_numeric_range
from .anonymizer.lib.pseudonymization import pseudonymize_columns, pseudonymize_rows
from .anonymizer.lib.swapping import swap_columns, swap_rows

ALGORITHM_FUNCTIONS = {
    'encrypt.chacha20': encrypt_chacha20,
    'encrypt.aes': encrypt_aes,
    'encrypt.salsa20': encrypt_salsa20,
    'generalize.percent': percent_generalization,
    'generalize.age': age_generalization,
    'hash.md5': apply_md5,
    'hash.sha1': apply_sha1,
    'hash.sha256': apply_sha256,
    'mask.full': mask_full,
    'mask.range': mask_range,
    'mask.first_n_characters': mask_first_n_characters,
    'mask.last_n_characters': mask_last_n_characters,
    'mask.email': mask_email,
    'mask.cpf': mask_cpf,
    'null_out.columns': drop_columns,
    'perturb.date': perturb_date,
    'perturb.numeric_range': perturb_numeric_range,
    'perturb.numeric_gaussian': perturb_numeric_gaussian,
    'perturb.numeric_laplacian': perturb_numeric_laplacian,
    'pseudonymize.columns': pseudonymize_columns,
    'pseudonymize.rows': pseudonymize_rows,
    'swap.columns': swap_columns,
    'swap.rows': swap_rows
}


def fetch_data(object):
    semaphore = Semaphore()

    futures = []

    start = time.perf_counter()
    df = value_to_dataframe(object["data"])
    with ThreadPoolExecutor() as executor:
        for parameter_id, parameter in enumerate(object["execution_parameters"], start=1):
            algorithm = parameter.get('algorithm', {})
            configuration = parameter.get('configuration', {})
            configuration.update({"parameter_id": parameter_id})
            columns = parameter.get('columns', {})
            future = executor.submit(
                apply_algorithm, algorithm, configuration, columns, df, semaphore, parameter_id
            )
            futures.append(future)
    wait(futures)
    end = time.perf_counter()
    response_time = (end - start) * 1000

    return format(response_time, '.3f').replace('.', ',')

def apply_algorithm(algorithm, configuration, columns, df, semaphore, parameter_id):
    """
    Apply the specified algorithm to the DataFrame using the provided configuration and columns.

    Args:
        algorithm (str): Name of the algorithm to apply.
        configuration (dict): Algorithm-specific configuration parameters.
        columns (dict): Column-specific configuration parameters.
        df (pd.DataFrame): DataFrame containing the data to be processed.
        parameter_id (int): ID of the current processing parameter.

    Return:
        None
    """

    algorithm_function = ALGORITHM_FUNCTIONS.get(algorithm)


    if algorithm_function:
        try:
            algorithm_function(df, columns, semaphore, **configuration)
        except ValueError as ve:
            error_message = str(ve)
        except Exception as e:
            error_message = "Unespected Error: " + str(e)
    else:
        error_message = "Invalid algorithm name:" + str(algorithm)

    if error_message:
        error_info = {
            "parameter_id": parameter_id,
            "algorithm": algorithm,
            "error_message": error_message
        }
        print(str(error_info))

    return None
