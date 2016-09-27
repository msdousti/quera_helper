import shutil
import os


def create_zip_file(L):
    """Creates a ZIP file based on the list L.
    This ZIP file has the 'test structure' specified in:
    https://github.com/mjnaderi/Sharif-Judge/blob/docs/v1.4/tests_structure.md

    Args:
        L:  A list containing pairs of strings.
            The 1st element in the pair is the input.
            The 2nd element in the pair is the corresponding output.

    Returns:
        Nothing.
    """
    shutil.rmtree('problem', True)
    os.makedirs('problem/in/')
    os.makedirs('problem/out/')

    i = 0
    for inp, outp in L:
        i += 1
        with open('problem/in/input{}.txt'.format(i), 'w') as f:
            f.write(str(inp))
        with open('problem/out/output{}.txt'.format(i), 'w') as f:
            f.write(str(outp))

    shutil.make_archive('problem', 'zip', 'problem')
    shutil.rmtree('problem', True)
