from pdfjin_pdf_to_powerpoint.core import pdf_to_powerpoint


def test_import():
    assert callable(pdf_to_powerpoint)
