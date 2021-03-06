"""
    sphinx.ext.githubpages
    ~~~~~~~~~~~~~~~~~~~~~~

    To publish HTML docs at GitHub Pages, create .nojekyll file.

    :copyright: Copyright 2007-2018 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import os

import sphinx

if False:
    # For type annotation
    from typing import Any, Dict  # NOQA
    from sphinx.application import Sphinx  # NOQA
    from sphinx.environment import BuildEnvironment  # NOQA


def create_nojekyll(app, env):
    # type: (Sphinx, BuildEnvironment) -> None
    if app.builder.format == 'html':
        path = os.path.join(app.builder.outdir, '.nojekyll')
        open(path, 'wt').close()


def setup(app):
    # type: (Sphinx) -> Dict[str, Any]
    app.connect('env-updated', create_nojekyll)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
