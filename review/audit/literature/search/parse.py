import sys,re,html
s=sys.stdin.buffer.read().decode("utf-8","replace")
for m in re.finditer(r'<td class="snipp"><a href="paper.jsp\?r=([^&]+)&.*?<span class="author">(.*?)</span>,\s*<span class="title">(.*?)</span>\s*\(<span class="year">(\d+)</span>\).*?<span class="snippet">(.*?)</span>', s, re.S):
    f=lambda x: re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>","",x))).strip()
    print(f"- {m.group(1)} | {m.group(4)} | {f(m.group(2))[:80]} | {f(m.group(3))}\n    snippet: {f(m.group(5))[:300]}")
