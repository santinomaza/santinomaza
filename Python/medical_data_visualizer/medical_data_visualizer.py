import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv', sep=',')

# 2
df['overweight'] = df['weight'] / (df['height'] / 100) ** 2
df['BMI'] = np.where(df['overweight'] > 25, 1, 0)

# 3
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5 & 6 & 7 & 8 & 9
    df_cat = pd.melt(
        df,
        id_vars=['id', 'cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
        var_name='health_factor',
        value_name='status_value'
    )

    df_cat['status'] = df_cat['status_value'].map({0: 'good', 1: 'bad'})

    g = sns.catplot(
        x='health_factor',
        hue='status',
        col='cardio',
        data=df_cat,
        kind='count',
        palette={'good': 'green', 'bad': 'red'},
        height=5,
        aspect=1.5,
        order=['cholesterol', 'gluc', 'overweight', 'smoke', 'alco', 'active']
    )
    
    g.set_axis_labels("Health Factor", "Count")
    g.set_titles("Cardiovascular Status: {col_name}")
    g.fig.suptitle("Health Risk Factors Distribution by Cardiovascular Condition", y=1.05)
    
    for ax in g.axes.flat:
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    
    plt.tight_layout()
    
    g.savefig('catplot.png', dpi=300, bbox_inches='tight')
    
    return g.fig

fig = draw_cat_plot()
plt.show()
    
# 10 & 11 & 12 & 13 & 14 & 15 & 16
def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ].copy()

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    plt.figure(figsize=(12, 10))

    heatmap = sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    fmt=".1f",
    cmap='coolwarm',
    center=0,
    square=True,
    linewidths=.5,
    cbar_kws={"shrink": 0.8}
    )

    heatmap.set_title('Correlation Heatmap Metrics', pad=20)

    fig = heatmap.get_figure()
    
    fig.savefig('catplot.png', dpi=300, bbox_inches='tight')
    
    return fig

heatmap_fig = draw_heat_map()
plt.show()
