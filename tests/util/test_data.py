# Copyright 2019-2020 by Christopher C. Little.
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

"""abydos.tests.util.test_prod.

This module contains unit tests for abydos.util._prod
"""

import pytest

import shutil
import tempfile
import urllib.error

from abydos.util._data import (
    download_package,
    list_available_packages,
    list_installed_packages,
    package_path,
)


class TestData:
    """Test cases for abydos.util._prod."""

    DEFAULT_URL = 'https://raw.githubusercontent.com/chrislit/'
    DEFAULT_URL += 'abydos-data/master/index.xml'

    def test_data(self):
        """Test abydos.util._data."""
        assert isinstance(list_installed_packages(), list)
        try:
            available = list_available_packages()
            default_available = list_available_packages(url=self.DEFAULT_URL)
        except urllib.error.URLError as exc:
            pytest.skip('abydos-data index unavailable: {}'.format(exc))
        assert isinstance(available, tuple)
        assert isinstance(default_available, tuple)

        download_package('all')
        assert package_path('wikitext_qgram')[-14:] == 'wikitext_qgram'
        with pytest.raises(FileNotFoundError):
            package_path('not_a_real_package')

        temppath = tempfile.mkdtemp()
        download_package('wikitext_qgram', data_path=temppath, force=True)
        download_package('wikitext_qgram', data_path=temppath)
        shutil.rmtree(temppath)

        with pytest.raises(ValueError):
            list_available_packages(url='file:///etc/passwd')
