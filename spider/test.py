import re

pattern = "课时：</td>\n<td valign='top'"
words = "课时：</td>\n<td valign='top' class='propValue g_minor' >\n<span>256小时</span>\n</td>"
r = re.findall(pattern, words)
a = 1