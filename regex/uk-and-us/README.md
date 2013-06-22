<p>US english and UK english differ in many aspects. One such aspect is the aversion towards use of <strong>se</strong> instead of <strong>ze</strong> as used in the UK. Given the UK format of a word that ends with <strong>ze</strong>, your task is to find out the count of all its UK and US variant in the given sequences.</p>

<p><strong>Input Format</strong></p>

<p>First line contains an integer N. N lines follow, each line contains a sequence of words (W) separated by a single space.<br>
Next lines contains an integer T. T testcases follow in a new line. Each line contains the <strong>UK</strong> spelling of a word (W’)</p>

<p><strong>Constraints</strong></p>

<p>1 &lt;= N &lt;= 10<br>
Each line doesn’t contain more than 10 words (W)<br>
Each character of W and W’ is a lowercase alphabet.<br>
If C is the count of the number of characters of W or W’, then<br>
1 &lt;= C &lt;= 20<br>
1 &lt;= T &lt;= 10<br>
W’ ends with <strong>ze</strong> (UK version of the word)</p>

<p><strong>Output Format</strong></p>

<p>Output T lines and in each line output the number of UK and US version of (W’) in all of N lines that contains a sequence of words.</p>

<p><strong>Sample Input</strong></p>

<pre><code>2
hackerrank ui is easy to familiarise with
to familiarize oneself with ui of hackerrank is easy
1
familiarize
</code></pre>

<p><strong>Sample Output</strong></p>

<pre><code>2
</code></pre>

<p><strong>Explanation</strong></p>

<p>In the given 2 lines, we find <em>familiarize</em> and <em>familiarise</em> once each. So, the total count is 2.</p>
