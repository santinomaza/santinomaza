import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
#df = None
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
# Clean data
#df = None
bottom_thresh = df['value'].quantile(0.025)
top_thresh = df['value'].quantile(0.975)

# Filter out the outliers
df_clean = df[
    (df['value'] >= bottom_thresh) & 
    (df['value'] <= top_thresh)
]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_clean.index, df_clean['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.tight_layout()
    return fig
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

fig = draw_line_plot()
plt.show()


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    #df_bar = None
    df_bar = df_clean.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    monthly_avg = (df_bar.groupby(['year', 'month'])['value'].mean().unstack()[month_order])
    
    fig = monthly_avg.plot(kind='bar', figsize=(12, 6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=month_order)
    plt.tight_layout()
    return fig
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
        
#bar_plot = draw_bar_plot()
#plt.show()

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df_clean.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
    
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    
    plt.tight_layout()
    return fig

    #fig = bar_plot.get_figure()
    #return fig
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
    #g.savefig('box_plot.png', dpi=300, bbox_inches='tight')
    
    #return g.fig

#box_plot = draw_box_plot()
#plt.show()
