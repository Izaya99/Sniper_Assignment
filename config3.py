cp ~/sniper-assignment/Sniper_Assignment/small.cfg .
python3 << 'EOF'
import re

with open('small.cfg', 'r') as f:
    content = f.read()

# L1 icache section
content = re.sub(r'(\[perf_model/l1_icache\].*?cache_size = )4', r'\g<1>64', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l1_icache\].*?associativity = )1', r'\g<1>4', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l1_icache\].*?data_access_time = )4', r'\g<1>12', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l1_icache\].*?tags_access_time = )1', r'\g<1>9', content, flags=re.DOTALL, count=1)

# L1 dcache section
content = re.sub(r'(\[perf_model/l1_dcache\].*?cache_size = )4', r'\g<1>64', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l1_dcache\].*?associativity = )1', r'\g<1>4', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l1_dcache\].*?data_access_time = )4', r'\g<1>12', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l1_dcache\].*?tags_access_time = )1', r'\g<1>9', content, flags=re.DOTALL, count=1)

# L2 cache section
content = re.sub(r'(\[perf_model/l2_cache\].*?cache_size = )32', r'\g<1>1024', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l2_cache\].*?associativity = )4', r'\g<1>8', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l2_cache\].*?data_access_time = )8', r'\g<1>18', content, flags=re.DOTALL, count=1)
content = re.sub(r'(\[perf_model/l2_cache\].*?tags_access_time = )3', r'\g<1>13', content, flags=re.DOTALL, count=1)

with open('small.cfg', 'w') as f:
    f.write(content)

print("Done!")
EOF
