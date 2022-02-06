from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.jason.return_value={
        'login': 'JonathansManoel', 'id': 96275361,
        'avatar_url': 'https://avatars.githubusercontent.com/u/96275361?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('jonathansmanoel')
    assert 'https://avatars.githubusercontent.com/u/96275361?v=4' == url



