import  pytest
import src.DB;
import src.Person
from mock import Mock
@pytest.fixture
def mock_db(db=data):
    return Mock(db)
def test_save(mock_db):
    gabe=Person("Gabe",mock_db)
    gabe.save();
    mock_db.persist.assert_called_with(gabe)