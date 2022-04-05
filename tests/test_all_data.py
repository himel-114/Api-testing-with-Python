import allure
# from test_data.user_api.country_api_data import *
from test_data.user_api.country_api_data import response_get_all_data


@allure.step('response_get_all_data')
def test_bd():
    response_body, status_code = response_get_all_data()
    print(response_body)
    print("\n")
    assert status_code == 200
    # print(response_body(["name"][0]))
    print(response_body[1]["name"]["nativeName"]["spa"]["common"])
    print("\n")
    # print(response_body[0]["name"]["nativeName"])
    # print("\n")
    # print(response_body[0]["name"]["nativeName"]["ben"])
    # print("\n")
    # print(response_body[0]["name"]["nativeName"]["ben"]["common"])
    #
    # assert type(response_body[0]["name"]) is dict
    # assert type(response_body[0]["name"]["nativeName"]) is dict
    # assert type(response_body[0]["name"]["nativeName"]["ben"]) is dict
    # assert type(response_body[0]["name"]["nativeName"]["ben"]["common"]) is str
    #
    # assert type(response_body[0]["name"]["official"]) != "People's Republic of Bangladesh"
    # assert type(response_body[0]["name"]["nativeName"]["ben"]["common"]) != "বাংলাদেশ"
    # assert type(response_body["articles"][0]["source"]["id"]) is str
    # # assert response_body["articles"][0] == response_body
    # # assert response_body["articles"][0]["id"] == "engadget"
    # for i in range(9):
    #     assert type(response_body["articles"][i]["source"]["name"]) is str
    #     assert type(response_body["articles"][i]["title"]) is str
    #     assert type(response_body["articles"][i]["description"]) is str
    #     assert type(response_body["articles"][i]["publishedAt"]) is str
