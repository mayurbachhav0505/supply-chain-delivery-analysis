# Supply Chain & Delivery Analytics

An operations analytics project analyzing 180,519 order records to understand delivery performance, replenishment risk, fulfillment-market reliability, and customer value through RFM segmentation.

## Project Overview

The project analyzes supply chain and order data to identify useful business insights related to:

- Delivery performance
- Shipping-mode reliability
- Regional delivery delays
- Replenishment risk
- Fulfillment-market reliability
- Customer RFM segmentation
- Revenue by customer segment

The analysis uses SQL with DuckDB as the primary analytical layer, Python for data processing and visualization, and Streamlit + Plotly for the interactive dashboard.

## Dataset

**Dataset:** DataCo Smart Supply Chain  
**Source:** [Kaggle - DataCo Smart Supply Chain](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)

- 180,519 order records
- 53 original columns

The dataset contains customer-related fields that are not required for analysis. Fields such as customer email, name, password, and address-related information are excluded when the data is loaded.

The raw dataset is not included in this repository because of its file size.

To download the dataset, run:

```bash
python python/download_data.py