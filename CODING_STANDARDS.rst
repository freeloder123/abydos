CODING STANDARDS
----------------

- Pytest will be used for testing.
- Ruff will be used for linting and best practice conformance.
- Pydocstyle will be used to ensure documentation style conformance to PEP257
  (for the most part) and NumPy documentation style.
- Ruff formatter will be used to keep code style consistent.
- 3rd party packages may be used, but must be present in both PyPI and conda
  or conda-forge. They must also support all supported Python versions.

----

git commits
~~~~~~~~~~~

Each commit should be a minimal unit of code or represent minimal changes.
Avoid doing multiple things in a single commit, but describe them in separate
lines of the commit log if this does occur.


git pushes
~~~~~~~~~~

A git push should be performed only under the following conditions:

- library is syntactically correct (compiling correctly) in both Python 3
- library passes all tests and doctests according to pytest in Python 3
- test coverage is 100% according to pytest
- ruff should report 0 issues
- ruff formatting has been applied


git history
~~~~~~~~~~~

Maintain a clean, informative commit history:

- Write commit messages in imperative mood (e.g., "Add validation to Soundex"
  not "Added validation to Soundex")
- Keep the subject line under 72 characters
- Use the body to explain *why* a change was made, not just *what* changed
- Reference issue numbers where applicable (e.g., "Fix #42")
- Avoid squashing unrelated changes into a single commit
- Rebase feature branches before merging to maintain a linear history
- Never force-push to shared branches (main, develop)


Notes on architecture
~~~~~~~~~~~~~~~~~~~~~

As of the 0.3.6 release, each major algorithm of the compression, distance,
fingerprint, phonetic, & stemmer subpackages has been moved into a class of its
own. The distance, fingerprint, phonetic, & stemmer classes each inherit from
respectively common classes that define basic methods for these four major
types of classes.

The old functional API for these subpackages was removed in version 0.6.

Although, as of the 0.3.6 release, many of the classes that have are pre-0.3.6
functions encapsulated in a class simply consist of a single method that
could be a static method, making these methods static is generally avoided.
As development continues, these classes will take more advantage of object
architecture to store parameters between calls and inherit from base classes.
