import string
import time
from functools import wraps


def timeit(nanoseconds: bool = False):
    """Decorator which outputs the execution time of a particular function in nanoseconds."""

    def timeit_wrapper(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            if nanoseconds:
                start_time: int = time.perf_counter_ns()
                result = func(*args, **kwargs)
                end_time: int = time.perf_counter_ns()
                total_time: int = end_time - start_time
                print(
                    f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} nanoseconds"
                )
            else:
                start_time: float = time.perf_counter()
                result = func(*args, **kwargs)
                end_time: float = time.perf_counter()
                total_time: float = end_time - start_time
                print(
                    f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds"
                )

            return result

        return func_wrapper

    return timeit_wrapper


def normalize_string(input_string: str) -> str:
    """Function which cleans the input string, removing puntuation and extra spaces. Returns a clean words string."""
    translation_table: dict[int, int] = str.maketrans(
        string.punctuation, " " * len(string.punctuation)
    )
    string_without_punc: str = input_string.translate(translation_table)
    string_without_double_spaces: str = " ".join(string_without_punc.split())
    return string_without_double_spaces.lower()


def url_scores_update(old: dict[str, float], new: dict[str, float]):
    """Function which helps updating old score values in the -url_scores- dictionary which in this case is -old-."""
    for url, score in new.items():
        if url in old:
            old[url] += score
        else:
            old[url] = score
    return old
