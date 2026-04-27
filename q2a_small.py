import re

with open('small.cfg', 'r') as f:
    content = f.read()

# L1 icache
content = re.sub(r'(\[perf_model/l1_icache\].*?cache_size = )4', r'\g<1>32', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l1_icache\].*?associativity = )1', r'\g<1>4', content, flags=re.DOTALL, count=1)

# L1 dcache
content = re.sub(r'(\[perf_model/l1_dcache\].*?cache_size = )4', r'\g<1>32', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l1_dcache\].*?associativity = )1', r'\g<1>4', content, flags=re.DOTALL, count=1)

# L2 cache
content = re.sub(r'(\[perf_model/l2_cache\].*?cache_size = )32', r'\g<1>256', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l2_cache\].*?associativity = )4', r'\g<1>8', content, flags=re.DOTALL, count=1)

with open('small.cfg', 'w') as f:
    f.write(content)

print("Done!")
