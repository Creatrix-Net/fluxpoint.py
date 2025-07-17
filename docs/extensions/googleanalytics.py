#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sphinx.errors import ExtensionError


def add_ga_javascript(app, pagename, templatename, context, doctree):
    if not app.config.GOOGLEANALYTICS_ENABLED:
        return

    metatags = context.get("metatags", "")
    metatags += (
        """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>"""
        % app.config.GOOGLEANALYTICS_ID
    )
    metatags += (
        """
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', '%s');
    </script>
    """
        % app.config.GOOGLEANALYTICS_ID
    )
    context["metatags"] = metatags


def check_config(app):
    if app.config.GOOGLEANALYTICS_ENABLED and not app.config.GOOGLEANALYTICS_ID:
        raise ExtensionError(
            "'GOOGLEANALYTICS_ID' config value must be set for ga statistics to function properly."
        )


def setup(app):
    app.add_config_value("GOOGLEANALYTICS_ID", "", "html")
    app.add_config_value("GOOGLEANALYTICS_ENABLED", True, "html")
    app.connect("html-page-context", add_ga_javascript)
    app.connect("builder-inited", check_config)
    return {
        "version": "0.3",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }