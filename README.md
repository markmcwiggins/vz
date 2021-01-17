# vz
Upgraded code to show Verizon

This version is restructured significantly:

- pylint checker gives 8.11 / 10 (default settings)
- uses a modification of the Family structure to point 'down' from parents to children to allow a more efficient 'walk'
- a few comments and Docstrings added

This one should run on the order of O(n), unlike the first version of O(WTF? -- not even focused on this)

To run:

python3 ./hierarchy.py data.in

Clearly: this hasn't been extensively tested, with just the one record. :-)