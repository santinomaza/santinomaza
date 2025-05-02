import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    #Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df, label='Data Points')
        
    #First line
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = range(1880, 2051)
    ax.plot(years_all, slope_all * years_all + intercept_all, 'r', label=f'All Data Fit (R²={linregress(df["Year"], df["CSIRO Adjusted Sea Level"]).rvalue**2:.2f})')
    
    #Second line
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    ax.plot(years_recent, slope_recent * years_recent + intercept_recent, 'g--', label=f'Post-2000 Fit (R²={linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]).rvalue**2:.2f})')
    
    #Format Labels Title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Create scatter plot


    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()