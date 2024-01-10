# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 05:31:29 2024

@author: Bharani
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def read_data(file_path):
    """
    Reads a CSV file and returns a Pandas DataFrame.
    
    Parameters:
    file_path: The path to the CSV file.
    A Pandas DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(file_path)

def plot_bar(data, x, y, title, xlabel, ylabel, color, ax):
    """
   Plots a bar chart.
   
   Parameters:
    data: The DataFrame containing the data.
    x : The column name for the x-axis.
    y : The column name for the y-axis.
    title : The title of the plot.
    xlabel : The label for the x-axis.
    ylabel : The label for the y-axis.
    color: The color of the bars.
    ax : The AxesSubplot on which the plot will be drawn.
   """
    sns.barplot(x=data[x], y=data[y], color=color, ax=ax)
    ax.set_title(title, fontsize=20, weight='bold')
    ax.set_xlabel(xlabel, fontsize=18)
    ax.set_ylabel(ylabel, fontsize=18)
    ax.tick_params(axis='x', rotation=45, labelsize=16)
    ax.tick_params(axis='y', labelsize=16)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.spines['top'].set_visible(False)  
    ax.spines['right'].set_visible(False)  
    ax.set_facecolor('#F8F8F8')  

def plot_line_avg_attack_by_age(df, ax):
    """
    Plots a line chart for average attack score by age.
    
    Parameters:
     df : The DataFrame containing player statistics.
     ax : The AxesSubplot on which the plot will be drawn.
    """
    avg_attack_by_age = df.groupby('Age')['Attack'].mean()
    sns.lineplot(x=avg_attack_by_age.index, y=avg_attack_by_age.values, marker='o', color='black', linestyle='-', linewidth=2, label='Average Attack Score', ax=ax)
    ax.set_title('Average Attack Score by Age', fontsize=20, weight='bold')
    ax.set_xlabel('Age', fontsize=18)
    ax.set_ylabel('Average Attack Score', fontsize=18)
    ax.tick_params(axis='x', rotation=45, labelsize=16)
    ax.tick_params(axis='y', labelsize=16)
    ax.legend(fontsize=16)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.spines['top'].set_visible(False) 
    ax.spines['right'].set_visible(False) 
    ax.set_facecolor('#F8F8F8')

def plot_horizontal_bar_avg_attack_block_by_country(df, ax, top_countries=10):
    """
    Plots a horizontal bar chart for top countries based on average attack and block scores.
    
    Parameters:
     df : The DataFrame containing player statistics.
     ax : The AxesSubplot on which the plot will be drawn.
     top_countries : The number of top countries to display is 10.
    """
    avg_attack_by_country = df.groupby('Country')['Attack'].mean().nlargest(top_countries)
    avg_block_by_country = df.groupby('Country')['Block'].mean().nlargest(top_countries)
    merged_df = pd.concat([avg_attack_by_country, avg_block_by_country], axis=1)
    merged_df.columns = ['Average Attack', 'Average Block']
    sns.barplot(data=merged_df.reset_index(), y='Country', x='Average Attack', color='skyblue', label='Average Attack', ax=ax)
    sns.barplot(data=merged_df.reset_index(), y='Country', x='Average Block', color='orange', label='Average Block', ax=ax)
    ax.set_title(f'Top {top_countries} Countries: Average Attack and Block', fontsize=20, weight='bold')
    ax.set_xlabel('Average Score', fontsize=18)
    ax.set_ylabel('Country', fontsize=18)
    ax.tick_params(axis='both', labelsize=16)
    ax.legend(fontsize=16, loc='upper right', facecolor='#F8F8F8') 
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_facecolor('#F8F8F8') 

def plot_piechart_position_distribution(df, ax):
    """
    Plots a pie chart for player position distribution.
    
    Parameters:
     df : The DataFrame containing player statistics.
     ax : The AxesSubplot on which the plot will be drawn.
    """
    position_distribution = df['Position'].value_counts()
    wedges, texts, autotexts = ax.pie(position_distribution, labels=position_distribution.index, autopct='%1.2f%%', startangle=140, colors=sns.color_palette('pastel'), textprops={'fontsize': 16})
    ax.set_title('Player Position Distribution', fontsize=20, weight='bold')  
    legend = ax.legend(wedges, position_distribution.index, title='Positions', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=18, facecolor='#F8F8F8')  
    legend.get_title().set_fontsize(20)
    legend.get_title().set_fontweight('bold')
    for item in legend.get_texts():
        item.set_fontsize(18)
    ax.tick_params(axis='both', labelsize=16)
    ax.spines['top'].set_visible(False)  
    ax.spines['right'].set_visible(False)  
    ax.set_facecolor('#F8F8F8')  

def plot_histogram_age_distribution(df, ax):
    """
    Plots a histogram for age distribution of players.

    Parameters:
     df : The DataFrame containing player statistics.
     ax : The AxesSubplot on which the plot will be drawn.
    """
    sns.histplot(df['Age'], bins=20, kde=True, color='lightgreen', edgecolor='black', alpha=0.7, ax=ax)
    ax.set_title('Age Distribution of Players', fontsize=20, weight='bold')
    ax.set_xlabel('Age', fontsize=18)
    ax.set_ylabel('Frequency', fontsize=18)
    ax.tick_params(axis='x', rotation=45, labelsize=16)
    ax.tick_params(axis='y', labelsize=16)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.spines['top'].set_visible(False)  
    ax.spines['right'].set_visible(False)  
    ax.set_facecolor('#F8F8F8')  

def analyze_player_statistics(df):
    """
    Analyzes player statistics and creates an infographic with multiple subplots.

    Parameters:
     df : The DataFrame containing player statistics.
    """
    fig, axs = plt.subplots(2, 2, figsize=(18, 12), facecolor='#F0F0F0')
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.3, hspace=0.4)

    for ax in axs.flat:
        ax.set_facecolor('#F0F0F0')
        ax.patch.set_alpha(0.0)

    plot_line_avg_attack_by_age(df, axs[0, 0])
    plot_horizontal_bar_avg_attack_block_by_country(df, axs[0, 1], top_countries=10)
    plot_piechart_position_distribution(df, axs[1, 0])
    plot_histogram_age_distribution(df, axs[1, 1])

    plt.suptitle('Player Statistics Analysis', fontsize=24, weight='bold', y=1.02)

    for ax in axs.flat:
        ax.set_facecolor('#F0F0F0')  
    plt.tight_layout(rect=[0, 0, 0.9, 1])

    # Description
    description_text = """
    Name       : Bharanidharan Thirumaran
    Student ID : 22076992
    
    This infographic shows the average attack and block scores, player position distribution,  
    and age distribution of players in volleyball.
    
    Line Plot: Average Attack Score by Age
    The attack score tends to peak around 25 years old.
    Scores rise as players mature and decline for younger and older age groups.
    
    Horizontal Bar Plot: Top 10 Countries - Average Attack and Block
    France excels in attacking, while Japan stands out in blocking.
    A mix of experienced and younger players dominate the top countries.
    
    Pie Chart: Player Position Distribution
    Outside hitters (OH) dominate the player positions at 32.10%.
    Liberos (L) and setters (S) are the least common positions.

    Histogram: Age Distribution of Players
    The majority of players fall within the 17.5-20.0 age bracket.
    A significant portion of players are also in the 15.0-17.5 and 20.0-22.5 age ranges.
    """

    plt.figtext(0.92, 0.5, description_text, ha='left', va='center', fontsize=18, wrap=True, backgroundcolor='#F0F0F0', bbox=dict(facecolor='#F0F0F0', edgecolor='none', boxstyle='round,pad=0.5'))

    #plt.savefig("22076992.png", dpi=300, bbox_inches='tight', facecolor='#F0F0F0')

    plt.show()

# Read data
df = read_data(r"VNL2023.csv")
analyze_player_statistics(df)
