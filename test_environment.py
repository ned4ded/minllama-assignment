import sys
import subprocess

REQUIRED_PYTHON = "python3"


def main():
    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError("Unrecognized python interpreter: {}".format(REQUIRED_PYTHON))

    if system_major != required_major:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_major, sys.version
            )
        )
    else:
        print(">>> Development environment passes all tests!")

    try:
        subprocess.check_output(["poetry", "--version"])
        print(">>> Poetry is installed")
    except subprocess.CalledProcessError:
        print(">>> Poetry is not installed")


if __name__ == "__main__":
    main()
