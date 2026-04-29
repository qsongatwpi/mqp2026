import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    values = np.array([1, 2, 3, 4])
    squared = values ** 2

    assert squared.tolist() == [1, 4, 9, 16], "NumPy calculation failed"

    fig, axis = plt.subplots()
    axis.plot(values, squared, marker="o")
    axis.set_title("Dependency Smoke Test")
    axis.set_xlabel("x")
    axis.set_ylabel("x^2")
    plt.close(fig)

    print("Dependency test passed.")


if __name__ == "__main__":
    main()