# quera_helper

[Quera](https://quera.ir) is an online judge for C, C++, Java and Python programming courses. The source code is [freely available](https://github.com/mjnaderi/Sharif-Judge).

Any instructor wishing to use Quera has to provide it with a *test structure*, as specified in [their documentation](https://github.com/mjnaderi/Sharif-Judge/blob/docs/v1.4/tests_structure.md).

The test structure is a ZIP file, often containing two directories: `in`, and `out`. The input files reside in the `in` directory, while the corresponding results (the expected output) are to be found in the `out` directory.

Creating the test structure is often a tedious task, and that's where `quera_helper` comes to the rescue! It takes a list of input-output pairs, and generates the desired ZIP file. Here's a sample code showing the usage:

```python
import quera_helper as qh

input1 = 6
input2 = 11

output1 = 36
output2 = 121

L = [(input1, output1), (input2, output2)]
qh.create_zip_file(L)
```