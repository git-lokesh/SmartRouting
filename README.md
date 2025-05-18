# 🐜 ACO PathFinder: Ant Colony Optimization for Smart Routing

This project applies the **Ant Colony Optimization (ACO)** algorithm to solve shortest path problems in two different environments:

1. **Water Distribution Network** – A custom-built graph simulating a water pipeline layout.
2. **Real-world Road Network** – Loaded using OpenStreetMap data via the `osmnx` library, specifically focused on **Chennai, India**.

ACO is a bio-inspired algorithm that simulates the pheromone-based navigation behavior of ants to find optimal paths.

---

## 📁 Project Structure

```
aco_pathfinding/
├── aco_water_network.py     # ACO on a sample water network graph
├── aco_city_network.py      # ACO on real-world map data from OSM
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🚀 Features

- Implements ACO from scratch using `networkx`, `numpy`, and `random`.
- Supports both synthetic and real-world graphs.
- Visualizes paths using `matplotlib` (for water network) and `osmnx` (for city roads).
- Easily configurable parameters like number of ants, iterations, pheromone importance, etc.

---

## 🛠️ Installation (Conda Environment Recommended)

```bash
# Create and activate a new environment
conda create -n aco_env python=3.10
conda activate aco_env

# Install dependencies
pip install -r requirements.txt
```

---

## 📌 Example Usage

### Run ACO on Water Network

```bash
python aco_water_network.py
```

Output:
```
Best path from Reservoir to C: ['Reservoir', 'A', 'C']
Total pipe distance: 45
```

### Run ACO on Chennai Road Network

```bash
python aco_city_network.py
```

This fetches live OSM data and displays the optimized route using a map-based plot.

---

## 📷 Visual Output

- **Water Network**: Graph with red-highlighted optimal path.
- **City Network**: Real-world route highlighted on a city map.

---

## 🧪 Requirements

All dependencies are listed in `requirements.txt`:

```
networkx
matplotlib
numpy
osmnx
```

---

## 📍 Location-Based Routing Example

The city network example uses coordinates from **Chennai**:

- **Source**: 13.032230, 80.211797
- **Destination**: 13.035937, 80.204351

You can modify these to suit your location or region of interest.

---

## 📜 License

This project is open-source and free to use for academic or personal purposes.

---

## 👨‍💻 Authors

Made by [Lokesh](https://github.com/L0KESHprograms) and [Tharun](https://github.com/THARUN2004-star)
