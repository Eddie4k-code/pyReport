import os
import bs4
from enum import Enum
import collections


class Status(Enum):
    PASS = "PASS"
    FAIL = "FAIL"

    def __str__(self):
        return self.name

class Report:
    def __init__(self, name, path):
        self.name = name
        self.path = path


    def startReport(self):
        """
        Generates the HTML File for the Report
        """
        file = open(f'{self.path}/{self.name}.html', 'w')

        html_template = '<!DOCTYPE html><html><head><title>Automation Test Results</title><link rel="stylesheet" href="report.css"></head><body><h1>Automation Test Results</h1><table><tr><th>Test Case</th><th>Result</th><th>Fail Reason</th></tr></table></body></html>'


        file.write(html_template)

        file.close()

    def reportTestCase(self, title, result, reason=""):
        """
        Adds the test case to the report along with the result
        :param title: Title of the Test Case you were testing
        :param result: the result of the Test Case you were testing
        """

        with open(f"{self.name}.html") as inf:
            file = open(f"{self.path}/{self.name}.html")
            soup = bs4.BeautifulSoup(file)
            table = soup.select('table')

        new_test = soup.new_tag("tr")
        th1 = soup.new_tag("td")
        th1.append(f"{title}")
        th2 = soup.new_tag("td")
        th2.append(f"{result}")
        th3 = soup.new_tag("td")
        th3.append(f"{reason}")

        new_test.append(th1)
        new_test.append(th2)
        new_test.append(th3)

        soup.table.append(new_test)


        with open(f"{self.path}/{self.name}.html", 'w') as outf:
            outf.write(str(soup))


def addition(n1, n2 ):
    total = n1 + n2

    return total















