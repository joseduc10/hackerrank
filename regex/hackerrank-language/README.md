<p>Every submission at hackerrank has a field called language which indicates the language in which a hacker has made his submission at hackerrank</p>

<p>C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA<br>
BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC</p>

<p>Sometimes, error prone API requests has an invalid language field. Could you find out if a given submission has a valid language field or not.</p>

<p><strong>Input Format</strong></p>

<p>First line contains N. N API requests follow, each in a newline.
Each request has an integer api_id and a string <em>language</em> which are the request parameters placed by the an API request.</p>

<p><strong>Constraints</strong></p>

<pre><code>1 &lt;= N &lt;= 100  
10^4 &lt;= api_id &lt; 10^5  
</code></pre>

<p>a valid language is any of the languages listed above (case sensitive)</p>

<p><strong>Output Format</strong></p>

<p>For every api request given in input, print “VALID” if it has a valid language string in it or print “INVALID” otherwise.</p>

<p><strong>Sample Input</strong></p>

<pre><code>3
11011 LUA
11022 BRAINFUCK
11044 X
</code></pre>

<p><strong>Sample Output</strong></p>

<pre><code>VALID
VALID
INVALID
</code></pre>

<p><strong>Explanation</strong></p>

<p>LUA and BRAINFUCK are valid languages as listed above. As X is doesn’t appear in the list, it is an invalid request.</p>
