from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.grand_rapids_n_quarter_improvement import (
    GrandRapidsNQuarterImprovementSpider,
)

test_response = file_response(
    join(dirname(__file__), "files", "grand_rapids_n_quarter_improvement.html"),
    url="http://grandrapidscitymi.iqm2.com/Citizens/calendar.aspx?View=List",
)
spider = GrandRapidsNQuarterImprovementSpider()

freezer = freeze_time("2023-07-27")
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]

freezer.stop()


"""
Uncomment below
def test_tests():
    print("Please write some tests for this spider or at least disable this one.")
    assert False
"""


def test_title():
    assert parsed_items[0]["title"] == "N. Quarter Corridor Improvement Authority"


def test_description():
    assert parsed_items[0]["description"] == ""


def test_start():
    assert parsed_items[0]["start"] == datetime(2023, 1, 19, 16, 0)


# def test_end():
#     assert parsed_items[0]["end"] == datetime(2019, 1, 1, 0, 0)


def test_time_notes():
    assert parsed_items[0]["time_notes"] == ""


def test_id():
    assert (
        parsed_items[0]["id"]
        == "grand_rapids_n_quarter_improvement/202301191600/x/n_quarter_corridor_improvement_authority"  # noqa
    )


def test_status():
    assert parsed_items[0]["status"] == "passed"


def test_location():
    assert parsed_items[0]["location"] == {
        "name": "",
        "address": "Culver CPA Group 1419 Coit Ave NE, Grand Rapids, MI  49505",
    }


def test_source():
    assert (
        parsed_items[0]["source"]
        == "http://grandrapidscitymi.iqm2.com/Citizens/calendar.aspx?View=List"
    )


def test_links():
    assert parsed_items[0]["links"] == [
        {
            "href": "http://grandrapidscitymi.iqm2.com//Citizens/Detail_Meeting.aspx?ID=7235",  # noqa
            "title": "Meeting Page",
        },
        {
            "href": "http://grandrapidscitymi.iqm2.com//Citizens/Detail_Meeting.aspx?ID=7235",  # noqa
            "title": "Agenda",
        },
        {
            "href": "http://grandrapidscitymi.iqm2.com/Citizens/FileOpen.aspx?Type=1&ID=5156&Inline=True",  # noqa
            "title": "Agenda Packet",
        },
        {"href": None, "title": "Summary"},
        {
            "href": "http://grandrapidscitymi.iqm2.com/Citizens/FileOpen.aspx?Type=12&ID=5207&Inline=True",  # noqa
            "title": "Minutes",
        },
    ]


def test_classification():
    assert parsed_items[0]["classification"] == NOT_CLASSIFIED


@pytest.mark.parametrize("item", parsed_items)
def test_all_day(item):
    assert item["all_day"] is False
