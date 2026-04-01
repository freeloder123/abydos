:orphan:

Word-File Phonetic Coverage
===========================

This note compares the checklist in
``/Users/daniellopezdecastro/Desktop/Phonetic algorithms/Phonetic algorithms .docx``
against the phonetic algorithms exported by :py:mod:`abydos.phonetic`.

Covered directly
----------------

- Soundex (Original / American Soundex): :py:class:`abydos.phonetic.Soundex`
- Daitch-Mokotoff Soundex: :py:class:`abydos.phonetic.DaitchMokotoff`
- Cologne Phonetics (Kölner Phonetik): :py:class:`abydos.phonetic.Koelner`
- Metaphone: :py:class:`abydos.phonetic.Metaphone`
- Double Metaphone: :py:class:`abydos.phonetic.DoubleMetaphone`
- Metaphone 3: :py:class:`abydos.phonetic.Metaphone3`
- NYSIIS: :py:class:`abydos.phonetic.NYSIIS`
- Caverphone / Caverphone 2.0: :py:class:`abydos.phonetic.Caverphone`
- Beider-Morse Phonetic Matching (BMPM):
  :py:class:`abydos.phonetic.BeiderMorse`
- Match Rating Approach (MRA): :py:class:`abydos.phonetic.MRA`
- Eudex: :py:class:`abydos.phonetic.Eudex`
- Phonex: :py:class:`abydos.phonetic.Phonex`
- Phonem: :py:class:`abydos.phonetic.Phonem`
- Polyphon: :py:class:`abydos.phonetic.Polyphon`
- SfinxBis: :py:class:`abydos.phonetic.SfinxBis`
- ONCA (Oxford Name Compression Algorithm):
  :py:class:`abydos.phonetic.ONCA`

Covered via exported aliases
----------------------------

- AmericanSoundex and OriginalSoundex alias :py:class:`abydos.phonetic.Soundex`
- ColognePhonetics aliases :py:class:`abydos.phonetic.Koelner`
- Caverphone2 aliases :py:class:`abydos.phonetic.Caverphone`
- BMPM aliases :py:class:`abydos.phonetic.BeiderMorse`
- MatchRatingApproach aliases :py:class:`abydos.phonetic.MRA`
- CFE aliases :py:class:`abydos.phonetic.PhoneticSpanish`
- Polyphone aliases :py:class:`abydos.phonetic.Polyphon`

The CFE mapping is based on the Spanish phonetic implementation already present
in Abydos. The cited source in :py:class:`abydos.phonetic.PhoneticSpanish`
describes the proposed algorithm as ``PhoneticSpanish``.

Notes
-----

- ``Familia Soundex``, ``Familia Metaphone``, ``Algoritmos Especializados por Región``,
  and ``Otros Algoritmos`` are category headings in the Word document, not
  standalone algorithms.
- ``Polyphone`` in the Word checklist is covered via the upstream Russian
  ``Polyphon`` algorithm naming used by the public implementation and paper.
