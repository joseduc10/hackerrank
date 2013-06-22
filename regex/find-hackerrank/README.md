At HackerRank, we always want to find out how popular we are getting everyday and have scraped conversations from popular sites. Each conversation fits in 1 line and there are N such conversations. Each conversation has utmost 1 word that says hackerrank (all in lowercase). We would like you to help us figure out whether a conversation

1. Start with hackerrank
2. Ends with hackerrank
3. Start and ends with hackerrank

<b>Input Format</b>

First line of the input contains N, N lines follow. Second line onwards, each line contains a set of words W separated by a single space

Constraints

1 <= N <= 10

1 <= W <= 100

All the characters in W are lowercase alphabets. If C is the count of the characters in W, then 1 <= C <= 20

<b>Output Format</b>

For every line,

Print 1 if the conversation starts with hackerrank<br>
Print 2 if the conversation ends with hackerrank<br>
Print 0 if the conversation starts and ends with hackerrank<br>
Print -1 if none of the above.

Sample Input

4<br>
i love hackerrank<br>
hackerrank is an awesome place for programmers<br>
hackerrank<br>
i think hackerrank is a great place to hangout<br>

Sample Output

2<br>
1<br>
0<br>
-1<br>

Explanation

The first conversation ends with hackerrank and hence 2<br>
The second conversation starts with hackerrank and hence 1<br>
The third converstaion has only one word, it starts and ends with hackerrank and hence 0.<br>
The fourth conversation satisfies none of the above properties and hence -1.<br>
