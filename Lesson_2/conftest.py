import pytest

@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def btn_selector():
    return "button"

@pytest.fixture()
def result():
    return "401"

@pytest.fixture()
def hello_user():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""

@pytest.fixture()
def create_post_btn():
    return """#create-btn"""

@pytest.fixture()
def enter_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture()
def enter_desc():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture()
def enter_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def save_post_btn():
    return """#create-item > div > div > div:nth-child(7) > div > button > span"""


@pytest.fixture()
def post_name():
    return """//*[@id="app"]/main/div/div[1]/h1"""