import yaml
from module import Site
import time


with open("C:/Users/mVm/OneDrive/Рабочий стол/ОБУЧЕНИЕ/Автоматизация тестирования веб-приложений на Python (лекции)/DZ_web_application/Lesson_2/testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

# def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, result):
#     input1 = site.find_element("xpath", x_selector1)
#     input1.send_keys("test")
#     input2 = site.find_element("xpath", x_selector2)
#     input2.send_keys("test")
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#     err_label = site.find_element("xpath", x_selector3)
#     assert err_label.text == result
    
    # site.close()
    
def test_step2(x_selector1, x_selector2, btn_selector, hello_user):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["passwd"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    
    element = site.find_element("xpath", hello_user)
    assert element.text == f'Hello, {testdata["login"]}'
    
    # site.close()  
    
"""Задание: Добавить в наш тестовый проект шаг добавления поста после входа. 
Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста."""

def test_step3(create_post_btn, enter_title, enter_desc, enter_content, save_post_btn, post_name):
    
    create_posts = site.find_element("css", create_post_btn)
    create_posts.click()
    title = site.find_element("xpath", enter_title)
    title.clear()
    title.send_keys(testdata['title'])
    description = site.find_element("xpath", enter_desc)
    description.clear()
    description.send_keys(testdata['description'])
    content = site.find_element("xpath", enter_content)
    content.clear()
    content.send_keys(testdata['content'])
    save_posts_btn = site.find_element("css", save_post_btn)
    save_posts_btn.click()
    time.sleep(3)
    check_post = site.find_element("xpath", post_name) 
    assert check_post.text == f"{testdata['title']}" 
        
    site.close() 