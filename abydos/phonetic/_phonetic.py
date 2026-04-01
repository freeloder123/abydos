# Copyright 2018-2020 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.phonetic._phonetic.

The phonetic._phonetic module implements abstract class Phonetic.
"""

from itertools import groupby
from typing import Optional, Set

__all__ = ['_Phonetic']


class _Phonetic:
    """Abstract Phonetic class.

    .. versionadded:: 0.3.6
    .. versionchanged:: 0.6.0
        Added parameter validation methods and named constants
    """

    # Named constants for code length bounds
    MIN_CODE_LENGTH = 4
    MAX_CODE_LENGTH = 64
    UNLIMITED_LENGTH = -1

    # Valid Soundex variants
    SOUNDEX_VARIANTS = frozenset({'American', 'special', 'Census'})

    _uc_set = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    _lc_set = set('abcdefghijklmnopqrstuvwxyz')
    _uc_v_set = set('AEIOU')
    _lc_v_set = set('aeiou')
    _uc_vy_set = set('AEIOUY')
    _lc_vy_set = set('aeiouy')

    @staticmethod
    def _validate_word(word: str) -> None:
        """Validate that the input word is a string.

        Parameters
        ----------
        word : str
            The word to validate

        Raises
        ------
        TypeError
            If ``word`` is not a string

        .. versionadded:: 0.6.0

        """
        if not isinstance(word, str):
            raise TypeError(
                f'word must be a string, got {type(word).__name__}'
            )

    @classmethod
    def _validate_max_length(
        cls,
        max_length: int,
        min_length: Optional[int] = None,
        max_cap: Optional[int] = None,
    ) -> int:
        """Validate and clamp max_length to valid bounds.

        Parameters
        ----------
        max_length : int
            The requested maximum code length
        min_length : int, optional
            Minimum allowed length (defaults to MIN_CODE_LENGTH)
        max_cap : int, optional
            Maximum allowed length (defaults to MAX_CODE_LENGTH)

        Returns
        -------
        int
            The validated and clamped max_length value

        Raises
        ------
        TypeError
            If ``max_length`` is not an integer

        .. versionadded:: 0.6.0

        """
        if not isinstance(max_length, int):
            raise TypeError(
                'max_length must be an integer, got '
                f'{type(max_length).__name__}'
            )
        if min_length is None:
            min_length = cls.MIN_CODE_LENGTH
        if max_cap is None:
            max_cap = cls.MAX_CODE_LENGTH

        if max_length == cls.UNLIMITED_LENGTH:
            return max_cap
        return min(max(min_length, max_length), max_cap)

    def _delete_consecutive_repeats(self, word: str) -> str:
        """Delete consecutive repeated characters in a word.

        Parameters
        ----------
        word : str
            The word to transform

        Returns
        -------
        str
            Word with consecutive repeating characters collapsed to a single
            instance

        Examples
        --------
        >>> pe = _Phonetic()
        >>> pe._delete_consecutive_repeats('REDDEE')
        'REDE'
        >>> pe._delete_consecutive_repeats('AEIOU')
        'AEIOU'
        >>> pe._delete_consecutive_repeats('AAACCCTTTGGG')
        'ACTG'


        .. versionadded:: 0.1.0
        .. versionchanged:: 0.3.6
            Encapsulated in class

        """
        return ''.join(char for char, _ in groupby(word))

    def encode(self, word: str) -> str:
        """Encode phonetically.

        Parameters
        ----------
        word : str
            The word to transform

        Raises
        ------
        TypeError
            If ``word`` is not a string


        .. versionadded:: 0.3.6
        .. versionchanged:: 0.6.0
            Added input validation

        """
        self._validate_word(word)
        return word

    def encode_alpha(self, word: str) -> str:
        """Encode phonetically using alphabetic characters.

        Parameters
        ----------
        word : str
            The word to transform

        Returns
        -------
        str
            The word transformed


        .. versionadded:: 0.3.6

        """
        return self.encode(word)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
