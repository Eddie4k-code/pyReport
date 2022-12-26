# pyReport
Simple module / script that can be used to generate HTML reports for tests. Using BeautifulSoup


<h1>Instruction</h1>
<li>Create a Report object - test = Report(Filename, path)</li>
<li>Generate the HTML Report File - .startReport()</li>
<li>Add a test case to the report and the result - .reportTestCase(Test Case Name, pass/fail, Reason(Optional))</li>

<h1>Example</h1>
<p>Testing the function add which will add two numbers</p>
![image](https://user-images.githubusercontent.com/98666468/209576401-c66a4659-64ef-4731-a4da-f33a636feb99.png)
<p>In this situation, if the test case is as expected then it will be reported on the HTML file as a pass, if it fails then it will be reported on the html file as a Fail and a reason can be specified for the failure</p>

<h1>The HTML Report</h1>
<p></p>
