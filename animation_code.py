import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the Nobel Prize dataset
file_path = 'nobel.csv'
nobel_data = pd.read_csv(file_path)

# Filter relevant columns and clean the data
data = nobel_data[['year', 'birth_country']].dropna()
data['birth_country'] = data['birth_country'].str.strip()

# Count Nobel Prize winners by year and country
country_year_counts = (
    data.groupby(['year', 'birth_country'])
    .size()
    .reset_index(name='count')
)

# Cumulative count of prizes by country
country_year_counts['cumulative_count'] = (
    country_year_counts.groupby('birth_country')['count'].cumsum()
)

# Prepare data for animation
all_years = range(country_year_counts['year'].min(), country_year_counts['year'].max() + 1)
countries = country_year_counts['birth_country'].unique()

animated_data = pd.DataFrame()
for year in all_years:
    yearly_data = country_year_counts[country_year_counts['year'] <= year]
    cumulative = yearly_data.groupby('birth_country')['cumulative_count'].max().reset_index()
    cumulative['year'] = year
    animated_data = pd.concat([animated_data, cumulative], ignore_index=True)

animated_data = animated_data.fillna(0)

# Create the animation
fig, ax = plt.subplots(figsize=(10, 6))

def update(year):
    ax.clear()
    
    # Filter data for the current year
    current_data = animated_data[animated_data['year'] == year]
    current_data = current_data.sort_values(by='cumulative_count', ascending=False).head(10)

    # Plot the bar chart
    bars = ax.barh(current_data['birth_country'], current_data['cumulative_count'], color='skyblue')
    
    # Annotate the bars with the cumulative count, placing the text just beside the bar
    for bar, count in zip(bars, current_data['cumulative_count']):
        ax.text(
            bar.get_width() + 1,  # Position the text just outside the bar (to the right)
            bar.get_y() + bar.get_height() / 2,  # Center the text vertically on the bar
            f'{int(count)}',  # Text to display
            va='center',  # Vertical alignment
            ha='left',  # Horizontal alignment to position text on the left of the number
            fontsize=10  # Font size
        )
    
    # Add chart titles and labels
    ax.set_title(f'Nobel Prize Winners by Country - {year}', fontsize=16)
    ax.set_xlabel('Total Nobel Prizes', fontsize=12)
    ax.set_ylabel('Country', fontsize=12)
    ax.invert_yaxis()

ani = FuncAnimation(fig, update, frames=all_years, repeat=False)

# Save the animation as a video
ani.save('nobel_timeline.gif', writer='pillow', fps=4)
plt.close(fig)
