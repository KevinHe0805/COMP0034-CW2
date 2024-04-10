"""
Testing for database
"""

from oil_and_gas_app import db
from oil_and_gas_app.models import Source


def test_source_model(test_client):
    """
    Test Source database for oil and gas prices
    """
    source = Source(
        type="Gas",
        Date=20020805,
        Price=2.81
    )
    db.session.add(source)
    db.session.commit()

    # Retrieve the newly created Source instance from the database
    source_from_db = Source.query.filter_by(type="Gas").first()

    # Check that the source instance was correctly added to the database
    assert source_from_db is not None
    assert source_from_db.type == "Gas"
    assert source_from_db.Date == 20020805
    assert source_from_db.Price == 2.81

