<p>The equivalent of SSN in India is a PAN number, which is unique to each of its citizens. In any of the country’s official documents, the PAN number is listed as 
follows</p>

<pre><code>&lt;char&gt;&lt;char&gt;&lt;char&gt;&lt;char&gt;&lt;char&gt;&lt;digit&gt;&lt;digit&gt;&lt;digit&gt;&lt;digit&gt;&lt;char&gt;
</code></pre>

<p>Your task is to figure out if the PAN number is valid or not.
A valid PAN number will have all its alphabets in uppercase and digits
in the same order as listed above.</p>

<p><strong>Input Format</strong></p>

<p>First line contains N. N lines follow, each having a PAN number.</p>

<p><strong>Constraints</strong></p>

<p>1 &lt;= N &lt;= 10<br>
Each <em>char</em> is an alphabet (lowercase or uppercase)<br>
Each <em>digit</em> lies between 0 and 9<br>
The length of the PAN number is always 10<br>
Every character in PAN is either <em>char</em> or <em>digit</em> satisfying the above constraints.  </p>

<p><strong>Output Format</strong></p>

<p>For every PAN number listed, print <em>YES</em> if it is valid and <em>NO</em> if it isn’t.</p>

<p><strong>Sample Input</strong></p>

<pre><code>3
ABCDS1234Y
ABAB12345Y
avCDS1234Y
</code></pre>

<p><strong>Sample Output</strong></p>

<pre><code>YES
NO
NO
</code></pre>

<p>The first PAN number is valid since the first 5 characters are alphabets, the next 4 are digits and the last character is an alphabet with all the alphabets in uppercase.<br>
The second PAN number is invalid as the fifth character is a digit as opposed to an alphabet.<br>
The third PAN number though valid has <em>some</em> alphabets in lowercase. Hence, invalid.</p>
