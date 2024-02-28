import re
txt = """assdf dfs,sdf/sd.sd"""
pattern = re.sub("\s|[.]|[,]",":",txt)
print(pattern)