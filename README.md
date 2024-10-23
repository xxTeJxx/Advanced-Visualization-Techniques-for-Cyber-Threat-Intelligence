# Visualizing Intelligence Analysis and Investigation Techniques

This project focuses on enhancing cybersecurity practices by utilizing advanced data visualization techniques to analyze network traffic data. The goal is to develop interactive tools to assist cybersecurity analysts in identifying patterns, anomalies, and potential threats within large datasets. 

## Overview

The project, conducted during an internship, aims to provide visual insights into network traffic behavior using the CSE-CIC-IDS2018 dataset. The project involves data preprocessing, feature extraction, and the application of visualization libraries to create intuitive plots and graphs that aid in cybersecurity investigations.

## Project Objectives

- Analyze and visualize network traffic data to uncover patterns and identify different types of cyber-attacks.
- Implement visualization techniques that allow for efficient, proactive threat detection.
- Provide clear insights into key traffic features such as flow duration and attack distribution using industry-standard libraries.
- Present results in a professional manner for cybersecurity analysts to interpret and act upon.

## Tools and Technologies Used

- **Google Colab:** Utilized for data analysis, coding, and visualizations, leveraging cloud-based infrastructure for efficient execution.
- **Pandas:** For data loading, preprocessing, and manipulation of large network traffic datasets.
- **Seaborn & Matplotlib:** Used to create detailed visualizations, including histograms, count plots, box plots, pair plots, and heatmaps.
- **Parquet:** A columnar storage format that efficiently handles large datasets for analysis.

## Dataset Overview

The **CSE-CIC-IDS2018 dataset** is a comprehensive collection of network traffic data simulating real-world network activity, including both benign and malicious traffic. The dataset contains various attack types such as DoS, DDoS, Botnets, and Infiltration, and includes features like Flow Duration, Packet Size, and Total Forward Packets.

## Methodology

### Data Collection and Preprocessing
- Loaded Parquet files representing multiple days of network traffic data and merged them into a single DataFrame.
- Performed correlation analysis on numeric features and label encoding on attack types to prepare the data for machine learning tasks.
- Sampled large datasets to handle memory constraints in Google Colab while maintaining representative data subsets for analysis.

### Visualization Techniques
- **Flow Duration Distribution:** Created histograms to showcase the distribution of flow durations, highlighting traffic behavior.
- **Attack Type Distribution:** Used count plots to visualize the number of instances for each attack type.
- **Flow Duration by Attack Type:** Generated box plots to compare flow durations across different types of attacks.
- **Pairwise Feature Analysis:** Applied pair plots to investigate the relationships between key features, with attack types distinguished for better clarity.
- **Correlation Heatmap:** Displayed the top 10 correlated features with Flow Duration to help analysts focus on the most critical features in identifying cyber threats.

## Key Insights

- **Flow Duration:** Showed a skewed distribution, with a high number of short-duration flows, indicating high variability in traffic behavior.
- **Attack Distribution:** The dataset exhibited imbalanced attack types, with some attacks (e.g., DoS, DDoS) appearing more frequently than others.
- **Feature Correlation:** Flow Duration correlated significantly with features such as Total Forward Packets and Flow Bytes/s, which can be used to identify unusual network patterns.

## Conclusion

This project successfully implemented data preprocessing and visualization techniques to analyze network traffic and identify potential cyber threats. The visualizations provide valuable insights to cybersecurity professionals, helping them interpret complex datasets more effectively. The methodology and tools used are scalable and adaptable to larger datasets and real-time monitoring systems.

## Future Work

- Extend the project to incorporate **real-time traffic monitoring** for continuous cybersecurity analysis.
- Integrate machine learning models to **classify attack types** and predict threats based on traffic patterns.
- Enhance visualizations into **interactive dashboards** for dynamic exploration of network data by analysts.

## Status of the Project
**Completed with Testing**

## Link to Google Colab
[Google Colab Notebook](https://colab.research.google.com/drive/1hItvcUby8zgJczKGObhM3uTWbggbbIz0?usp=sharing)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- Thanks to **Moulya A S**, my project partner, for collaboration and support.
---
