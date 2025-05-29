# -*- coding: utf-8 -*-

from home_secret import api


def test():
    _ = api


if __name__ == "__main__":
    from home_secret.tests import run_cov_test

    run_cov_test(
        __file__,
        "home_secret.api",
        preview=False,
    )
