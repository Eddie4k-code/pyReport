# pyReport
Simple module / script that can be used to generate HTML reports for tests.

Dependencies - 
<li>BeautifulSoup (bs4)</li>

<h1>Instruction</h1>
<li>Create a Report object - test = Report(Filename, path)</li>
<li>Generate the HTML Report File - .startReport()</li>
<li>Add a test case to the report and the result - .reportTestCase(Test Case Name, pass/fail, Reason(Optional))</li>

<h1>Example</h1>
<p>Testing the function add which will add two numbers</p>
<img src="https://user-images.githubusercontent.com/98666468/209576410-6b5496f2-54e8-4393-a6e6-a63e7e8496dc.png" />
<p>In this situation, if the test case is as expected then it will be reported on the HTML file as a pass, if it fails then it will be reported on the html file as a Fail and a reason can be specified for the failure</p>

<h1>The HTML Report</h1>
<p>This is where all the results will be shown</p>
<img src="https://user-images.githubusercontent.com/98666468/209577887-d5462674-c98e-4aea-8feb-b11dcb28d068.png"/>
