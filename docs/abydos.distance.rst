abydos.distance package
=======================

.. automodule:: abydos.distance
    :members:
    :undoc-members:
    :show-inheritance:

.. _confusion_table:

2x2 Confusion Table Terms
-------------------------

Many token-based distance metrics in `abydos.distance` are described in terms
of a 2x2 confusion table over token membership in the source set `X`, target
set `Y`, and overall token alphabet `N`.

- `a = |X ∩ Y|` is the size of the intersection.
- `b = |X \ Y|` is the number of tokens found only in the source.
- `c = |Y \ X|` is the number of tokens found only in the target.
- `d = |(N \ X) \ Y|` is the number of tokens absent from both sets.
- `n = |N|` is the cardinality of the full alphabet.

.. _intersection_type:

Intersection Type
-----------------

Token-distance classes that accept `intersection_type` support these modes:

- `crisp`: ordinary set intersection where membership is binary.
- `fuzzy`: partial membership when similarity reaches a threshold; this uses a
  `metric` argument and, by default, a threshold of `0.8`.
- `soft`: partial membership weighted by token similarity; this uses a
  `metric` argument.
- `linkage`: group-linkage matching for similar tokens; this uses a `metric`
  argument and, by default, a threshold of `0.1`.

.. _alphabet:

Alphabet Parameter
------------------

Token-distance classes that accept `alphabet` use it to describe the universe
of possible tokens:

- If a `Counter` is supplied, it is used directly.
- If a collection is supplied, its cardinality is used.
- If an `int` is supplied, it is treated as the alphabet cardinality.
- If `None` is supplied, q-gram tokenizers infer a default alphabet size;
  otherwise the complement cardinality is treated as zero.
