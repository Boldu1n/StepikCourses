import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_lng_items(browser,language1):
    browser.get(link)
    lngs=dict()
    lngs={'ar':'أضف الى سلة التسوق', 'ca':'Afegeix a la cistella', 'cs':'Vložit do košíku', 'da':'Læg i kurv', 'de':'In Warenkorb legen', 'en-gb':'Add to basket', 'el':'Προσθήκη στο καλάθι', 'es':'Añadir al carrito', 'fi':'Lisää koriin', 'fr':'Ajouter au panier', 'it':'Aggiungi al carrello', 'ko':'장바구니 담기', 'nl':'Voeg aan winkelmand toe', 'pl':'Dodaj do koszyka', 'pt':'Adicionar ao carrinho', 'pt-br':'Adicionar à cesta', 'ro':'Adauga in cos', 'ru':'Добавить в корзину', 'sk':'Pridať do košíka', 'uk':'Додати в кошик', 'zh-hans':'Add to basket'}
    time.sleep(1) 
    a1=browser.find_element(By.CSS_SELECTOR, "[value={}]".format(str(language1)))#выбор языка
    a1.click()
    time.sleep(3)
    but=browser.find_element_by_css_selector("button.btn.btn-default")#смена языка на сайте
    but.click()    
    time.sleep(3)       
    but2=str(browser.find_element_by_css_selector('button.btn.btn-lg.btn-primary.btn-add-to-basket').text)#текст на кнопке
    assert but2==lngs.get(str(language1)), but2
    time.sleep(1)
    