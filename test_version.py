import pytest
import itertools

from bump import version
from bump import errors


def test_basic_good():
    good = [
        "0.3.4",
        "v2.12.3"
    ]
    versions = map(version.SemanticVersion, good)
    assert str(versions[0]) == "v"+good[0]
    assert str(versions[1]) == good[1]
    assert versions[0].major == 0
    assert versions[0].minor == 3
    assert versions[0].patch == 4

def test_explicit_constructor():
    versions = [
        version.SemanticVersion("2","12", "3","v"),
        version.SemanticVersion("2","12", "3"),
        version.SemanticVersion("2.12.3"),
        version.SemanticVersion("v2.12.3"),
    ]
    for first, second  in itertools.combinations(versions, r=2):
        assert first == second    

def test_prefix():
    raw = "0.3.4"
    ver = version.SemanticVersion(raw)
    assert ver == "v"+raw
    assert ver.prefix == "v"
    ver.prefix = "v-no"
    assert ver == "v-no"+raw
    ver.prefix = ""
    assert ver == raw

def test_eq():
    ver0 = version.SemanticVersion("2","12", "3","v")
    ver1 = version.SemanticVersion("2","12", "3","v")
    assert ver0 == ver1
    assert ver0 == str(ver1)
    assert str(ver0) == ver1
    assert str(ver0) == str(ver1)
    assert ver0 == ver0
    assert ver1 == ver1

def test_basic_bad():
    bad = [
        "3.3.4.5",
        "0.3.4v",
        "2.2",
        "aa3aa2.3.2"
    ]
    for b in bad:
        with pytest.raises(errors.InvalidVersionString):
            version.SemanticVersion(b)

def test_increment():
    raw = "v4.2.123"
    ver = version.SemanticVersion(raw)
    ver.patch += 1
    assert ver == "v4.2.124"

    ver.minor += 1
    assert ver == "v4.3.124"

