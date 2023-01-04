import pandas as pd
df = pd.read_csv("https://reneshbedre.github.io/assets/posts/anova/onewayanova.txt", sep="\t")
# Bruker pandas til å laste inn data, nedenfor er daten som blir hentet fra github.
"""
A	B	C	D
25	45	30	54
30	55	29	60
28	29	33	51
36	56	37	62
29	40	27	73
"""
# Endrer på structuren til dataframe for at statsmodels pakken lettere kan lese det
df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['A', 'B', 'C', 'D'])
# Endrer kolone navn
df_melt.columns = ['index', 'treatments', 'value']

from bioinfokit.analys import stat
# Dette er pakken vi trenger for å få ut de verdiene vi vil.

res = stat()
res.anova_stat(df=df_melt, res_var='value', anova_model='value ~ C(treatments)')
print(res.anova_summary)
# Dette lager ANOVA diagram med hjelp av bioinfokit v1.0.3 eller nyerer