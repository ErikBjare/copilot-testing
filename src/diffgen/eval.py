import subprocess


# Strings to strip everything after, during generation
STRIPS = [
    r"""if __name__ == "__main__":""",  # for Python init
    "main();",  # for javascript init
    "function test()",  # for javascript init
]

EXAMPLES = [1, 2]


def run_example(n: int):
    # run 1.py, read output
    output_py = subprocess.check_output(["python3", f"examples/{n}.py"])

    # run 1.js using node, read output
    output_js = subprocess.check_output(["node", f"examples/{n}.js"])

    assert output_py == output_js, (output_py, output_js)


def gen_prompt():
    """
    Generates a prompt for translation using the given examples.

    Tests and initialization/printing is stripped out to avoid leaking info to the model about external constraints.
    """
    output = ""
    for n in EXAMPLES:
        # open 1.py, read contents
        with open(f"{n}.py", "r") as f:
            contents_py = f.read()

        # open 2.py, read contents
        with open(f"{n}.js", "r") as f:
            contents_js = f.read()

        # strip everything after STRIPS
        for s in STRIPS:
            contents_py = contents_py.split(s)[0]
            contents_js = contents_js.split(s)[0]

        output += (
            "\n"
            + contents_py.strip()
            + "\n\n\n"
            + "# translate the function to javascript"
            + '\n"""\n'
            + contents_js.strip()
            + '\n"""\n'
            + "\n"
        )
    return output.strip()


def test_examples():
    for n in EXAMPLES:
        run_example(n)


if __name__ == "__main__":
    print(gen_prompt())
