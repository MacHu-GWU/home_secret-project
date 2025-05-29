# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from home_secret.tests import run_cov_test

    run_cov_test(
        __file__,
        "home_secret",
        is_folder=True,
        preview=False,
    )
