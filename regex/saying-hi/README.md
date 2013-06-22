<p>You are given N lines and your task is to find out which of the N lines starts
with</p>

<pre><code>hi&lt;BLANK&gt;
</code></pre>

<p>where <em>hi</em> is case-insensitive and is <strong>not</strong> immediately followed by the letter <strong>D</strong>
which is also case-insensitive</p>

<p><strong>Input Format</strong></p>

<p>First line contains an integer N, N lines follow each line with a sentence not more than 
10 words W each, separated by a single space</p>

<p><strong>Constraints</strong></p>

<p>1 &lt;= N &lt;= 10<br>
If C is the count of the number of words W in every sentence, then<br>
1 &lt;= C &lt;= 10<br>
Each non-empty character in W is either a lowercase or an uppercase alphabet only</p>

<p><strong>Output Format</strong></p>

<p>Print each line that satisfies the constraint as mentioned in the problem statement.</p>

<p><strong>Sample Input</strong></p>

<pre><code>5
Hi Alex how are you doing
hI dave how are you doing
Good by Alex
hidden agenda
Alex greeted Martha by saying Hi Martha
</code></pre>

<p><strong>Sample Output</strong></p>

<pre><code>Hi Alex how are you doing
</code></pre>

<p>The first line satisfies the constraint mentioned in the problem statement.<br>
Second line fails as it has d following </p>

<pre><code>hi&lt;blank&gt;
</code></pre>

<p>Third line fails as it doesn’t start with <em>h</em><br>
Fourth fails as the third character in the line is not empty ( BLANK )<br>
Fifth is not included in the answer as <em>Hi Martha</em> doesn’t appear at the beginning of the line.</p>
