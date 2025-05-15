# Visualizing Data with Python using Matplotlib and Plotly

This project demonstrates how to use Python's powerful visualization libraries—**Matplotlib** and **Plotly**—to explore and present various types of data. It includes hands-on examples such as plotting random walks, visualizing dice roll simulations, analyzing real-world weather data, and mapping recent earthquakes using GeoJSON data.

---

## 🛠 Technologies Used

- Python 3.x
- [Matplotlib](https://matplotlib.org/)
- [Plotly](https://plotly.com/python/)
- `csv` module
- `json` module
- Public datasets (Sitka Weather CSV, USGS Earthquake JSON)

---

## 📊 Visualizing Data with Python

### 1. **Plotting a Simple Line Graph**

- Plotted the **Fibonacci sequence**: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34`.
- Used **Matplotlib** to create a basic line graph.
- Customized the chart with titles, labels, and improved visual design for clarity.

### 2. **Random Walk Visualizations**

- Simulated a **random walk** — a path formed by a sequence of random steps.
- Created a visually appealing plot using Matplotlib to show the direction and distance of each walk.
- Color gradients were used to represent the progression of the walk.

### 3. **Rolling Dice with Plotly**

- Simulated **rolling two dice** and tracked outcomes.
- Created **interactive bar charts** using **Plotly Express** to show the frequency of each possible result.
- Included hover effects to enhance data readability in the browser with responsive design.

### 4. **Weather Data Analysis (CSV)**

- **Dataset:** Sitka, Alaska historical weather data (high and low temperatures).
- Visualized **temperature trends over time** using line charts.
- Practiced handling missing data, used the `datetime` module, and plotted **multiple data series** for comparison.

### 5. **Mapping Global Earthquakes (GeoJSON)**

- **Dataset:** Recent earthquake data from USGS in **GeoJSON** format.
- Parsed the data using Python’s `json` module.
- Created an **interactive world map** using `Plotly`'s `scatter_geo()` to show:
  - **Location** of each earthquake.
  - **Magnitude** represented by marker size and color.
- Clear visualization of **global earthquake distribution** over the past month.

---

📷 Screenshots
- https://github.com/b-mahadevan/visualizing_data_with_python/blob/main/weather_data/output3.png
- https://github.com/b-mahadevan/visualizing_data_with_python/blob/main/earthquake_data/eq_data_30_day/output.png

---

## 🚀 Future Work

- Integrate Seaborn for statistical plots.
- Add more real-time APIs for weather and earthquakes.
- Build a simple dashboard using Dash or Streamlit.

---





