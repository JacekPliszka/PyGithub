# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Jacek Pliszka (JacekPliszka@github)                           #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import re

import github.GithubObject


class ArtifactFile:
    """
    This class represents artifact file
    """
    filename = None
    data = None

    def __init__(self, header, data):
        self.data = data
        content_disposition = None
        for key, value in header.items():
            if key.lower() == 'content-disposition':
                match = next(re.finditer('filename=([^;]+)', value))
                if match:
                    self.filename = match.group(1)


class Artifact(
    github.GithubObject.CompletableGithubObject,
    metaclass=github.GithubObject.CompletableGithubObjectMeta
):
    """
    This class represents Artifacts.
    The reference can be found here https://developer.github.com/v3/actions/artifacts/
    """
    _ATTRIBUTES = {
        "id": "Int",
        "node_id": "String",
        "name": "String",
        "size_in_bytes": "Int",
        "url": "String",
        "archive_download_url": "String",
        "expired": "Bool",
        "created_at": "Datetime",
        "expires_at": "Datetime"
    }
    _artifact = None

    def get_artifact(self):
        if self._artifact is None:
            header, output = self._requester.requestMultipartBinaryAndCheck(
                "GET", self.archive_download_url
            )
            self._artifact = ArtifactFile(header, output)
        return self._artifact