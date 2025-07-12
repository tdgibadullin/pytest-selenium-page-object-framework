"""
Stores configuration constants such as URLs for testing.

Centralizes external links to simplify maintenance if they change.
"""

class Links:
    """Container for the URLs used by the automated tests."""

    # The URL of the web store's main page.
    MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"

    # The URL of the product page ("Coders at Work" book).
    PRODUCT_PAGE = (
        "http://selenium1py.pythonanywhere.com/catalogue/"
        "coders-at-work_207/"
    )
