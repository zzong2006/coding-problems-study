import numpy as np
from utils import cosine_similarity


def numpy_cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def test_cosine_similarity():
    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]
    np.testing.assert_almost_equal(
        cosine_similarity(vec1, vec2), numpy_cosine_similarity(vec1, vec2), verbose=True
    )
    print(f"\033[92mTest passed: {test_cosine_similarity.__name__}\033[0m")


def run_tests():
    test_cosine_similarity()


if __name__ == "__main__":
    run_tests()
