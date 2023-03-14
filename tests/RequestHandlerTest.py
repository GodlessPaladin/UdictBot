import RequestHandler as rh
from unittest.mock import ANY

# tests for wictionary module


def test1_wdict():
    assert rh.get_definition("Hawkeye") == ['A native or resident of the American state of Iowa.']


def test2_wdict():
    assert rh.get_definition("cold shoulder") == ['(idiomatic) A deliberate act of disrespect; a slight or snub']


def test3_wdict():
    assert rh.get_definition("scry") == ['To predict the future using crystal balls or other objects.',
                                         '(obsolete) To descry; to see.', '(obsolete) A cry or shout.',
                                         'A flock of wildfowl.']


def test4_wdict():
    assert rh.get_definition("balls to the wall") == ['(US, idiomatic, slang) With maximum effort or commitment.',
                                                   '(US, idiomatic, slang) Full throttle; (at) maximum speed. [since the 1960s]']


def test5_wdict_nodata():
    assert rh.get_definition("asdgdfhfg") == ["No definitions found"]

# tests for Urban Dictionary module


def test6_udict():
    assert rh.get_udict_definition("wat") == [ANY, ANY, ANY, ANY]


def test7_udict():
    assert rh.get_udict_definition("Ye Olde") == [ANY, ANY, ANY, ANY]


def test8_udict():
    assert rh.get_udict_definition("Turkey") == [ANY, ANY, ANY, ANY]


def test9_udict_nodata():
    assert rh.get_udict_definition("ahdgghdfghjk") == ["No definitions found"]

# combined tests


def test10_combined():
    assert type("\n".join(rh.get_definition("wat")) + "\n".join(rh.get_udict_definition("wat"))) is str


def test10_combined():
    assert "\n".join(rh.get_definition("fghfg")) + " " + "\n".join(rh.get_udict_definition("fghfg")) == "No definitions found No definitions found"
