from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner

from assertions import AssertionsTest
from searchtest import SearchTests


assertion_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)


smoke_test = TestSuite([assertion_test, search_test])
#TestSuite recibe la lista de variables donde se cargaron las pruebas

#Estos son los parametros para generar el reporte, solo se usa output en este caso y se indica el nombre del reporte
kwargs = {
    "output" : 'smoke-report'
}

#variable runner recibe los elementos para generar el reporte

runner = HTMLTestRunner(**kwargs)
#corremos el runner llamando a la suite de testing 'smoke-test'
runner.run(smoke_test)