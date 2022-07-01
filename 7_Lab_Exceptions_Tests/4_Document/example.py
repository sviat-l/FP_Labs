"""
Lab 7.4 Test Document
"""

from main import Document, Character


def test_document():
    """
    Test main classes and methods
    """
    print('Testing document methods...')
    doc = Document()
    doc.insert('h')
    doc.insert('e')
    doc.insert(Character('l', bold=True))
    doc.insert(Character('l', bold=True))
    doc.insert('o')
    doc.insert('\n')
    doc.insert(Character('w', italic=True))
    doc.insert(Character('o', italic=True))
    doc.insert(Character('r', underline=True))
    doc.insert('l')
    doc.insert('d')
    assert doc.string == 'he*l*lo\n/w/o_rld'
    doc.cursor.home()
    doc.delete()
    doc.insert('W')
    assert doc.string == "he*l*lo\nW/o_rld"
    doc.save()
    doc.characters[0].underline = True
    assert doc.string == "_he*l*lo\nW/o_rld"

    print('All tests passed!')

if __name__ ==  '__main__':
    test_document()
