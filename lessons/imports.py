"""Examples of importing Python."""

# from package import module/function
from lessons import helpers
from lessons import helpers as hp


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    # noting where the function is coming from
    print(f"The answer: {hp.THE_ANSWER}")


if __name__ == "__main__":
    main()