import pytest
from Invoice import Invoice

@pytest.fixture()
def productList1():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def productList2():
    products = {'Pencil': {'qnt': 15, 'unit_price': 4.00, 'discount': 7}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalucateTotalImpurePrice(invoice, productList1):
    invoice.totalImpurePrice(productList1)
    assert invoice.totalImpurePrice(productList1) == 75

def test_CanCalucateTotalDiscount(invoice, productList1):
    invoice.totalDiscount(productList1)
    assert invoice.totalDiscount(productList1) == 5.63

def test_CanCalucateTotalPurePrice(invoice, productList1):
    invoice.totalPurePrice(productList1)
    assert invoice.totalPurePrice(productList1) == 69.37

def test_CanAddAdditionalProduct(invoice, productList1, productList2):
    assert invoice.items == {}
    invoice.addAdditionalProduct(productList1)
    assert invoice.items == productList1
    invoice.addAdditionalProduct(productList2)
    combinedproductlist = productList1.copy()
    combinedproductlist.update(productList2.copy())
    assert invoice.items == combinedproductlist

def test_CanRemoveProduct(invoice, productList1, productList2):
    assert invoice.items == {}
    invoice.addAdditionalProduct(productList1)
    invoice.addAdditionalProduct(productList2)
    updatedproductlist = productList1.copy()
    updatedproductlist.update(productList2.copy())
    assert invoice.items == updatedproductlist
    invoice.removeProduct('Pencil')
    assert invoice.items == productList1

