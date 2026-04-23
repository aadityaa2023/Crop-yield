# Crop Yield and Price Prediction System

## 1. Project Overview
The Crop Yield and Price Prediction System is a web-based application designed to forecast crop yields and prices using historical data, environmental factors (such as rainfall), and time components. It leverages Machine Learning, specifically Decision Tree Regression, to empower farmers, agricultural planners, and stakeholders with actionable insights for 23 different commodities.

## 2. Objective
The primary goal of this project is to provide accurate and timely yield predictions for various crops. By analyzing past data, the system helps in making informed agricultural decisions, optimizing crop selection, and anticipating market trends.

## 3. Key Features
- **Comprehensive Dashboard:** Displays the Top 5 High-Yield and Top 5 Low-Yield crops based on the current month's forecast compared to the previous month.
- **Detailed Crop Profiles:** Offers an in-depth analysis of 23 different crops, including prime locations, crop types (Kharif/Rabi), export destinations, and high-quality images.
- **Short-Term & Long-Term Forecasting:** Provides a 6-month predictive forecast for all commodities and detailed 12-month historical and future trends for individual crops.
- **Dynamic Machine Learning Model:** Automatically trains a Decision Tree Regressor model upon initialization if a pre-trained model (`model.pkl`) is not found.
- **Interactive Visualizations:** Uses modern UI components to display yield data dynamically.

## 4. System Architecture
The application follows a client-server architecture:
- **Frontend:** Built with HTML, CSS, and Bootstrap, featuring interactive UI elements and charts for data visualization.
- **Backend:** Powered by Flask (Python). It handles routing, logic, and serves as an API layer for the frontend.
- **Machine Learning Layer:** Uses Scikit-Learn's Decision Tree Regressor to train models on historical crop data (CSV files). The models are serialized using Pickle for faster load times.

## 5. Technologies Used
- **Programming Language:** Python 3.x
- **Web Framework:** Flask
- **Data Manipulation & Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (Decision Tree Regressor)
- **Model Serialization:** Pickle
- **Frontend:** HTML5, CSS3, JavaScript (Chart.js for rendering graphs)

## 6. Dataset Description
The system relies on individual CSV datasets for 23 crops (e.g., Arhar, Bajra, Cotton, Wheat, Sugarcane).
Each dataset contains historical data featuring:
- **Month & Year:** The timeframe of the record.
- **Rainfall:** The annual/monthly rainfall data.
- **Yield/WPI (Wholesale Price Index):** The target variable that the model predicts.

## 7. Machine Learning Methodology
- **Algorithm:** Decision Tree Regressor
- **Why Decision Tree?:** It is highly capable of capturing non-linear relationships between independent variables (Time, Rainfall) and the dependent variable (Crop Yield).
- **Process:**
  1. **Data Preprocessing:** CSV files are read using Pandas. Features ($X$) and Target ($Y$) are separated.
  2. **Model Training:** `DecisionTreeRegressor` is instantiated with randomized depth parameters to prevent overfitting while capturing sufficient variance.
  3. **Evaluation:** The model calculates the $R^2$ accuracy score to measure prediction reliability.
  4. **Persistence:** The trained models for all 23 crops are saved into a `model.pkl` file to eliminate the need to retrain on every application startup.

## 8. Project Structure
```text
Crops/
│
├── static/               # Contains datasets (CSV) and static assets (images, css, js)
├── templates/            # HTML templates for the Flask app (index.html, commodity.html)
├── app.py                # Main Flask application and routing logic
├── crops.py              # Contains static information (locations, types, export info) for crops
├── generate_model.py     # Script to explicitly train the ML model and generate model.pkl
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 9. Setup and Installation

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation Steps
1. **Clone or Download the Repository:**
   Navigate to your desired directory and extract the project files.

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate the Machine Learning Model (Optional):**
   You can manually train the models to generate the `model.pkl` file before starting the app.
   ```bash
   python generate_model.py
   ```
   *Note: If you skip this step, `app.py` will automatically train the models upon the first run.*

5. **Run the Application:**
   ```bash
   python app.py
   ```

6. **Access the Application:**
   Open your web browser and navigate to: `http://127.0.0.1:5000/`

## 10. Future Enhancements
- **Integration of Live Weather API:** Incorporate real-time weather forecasting to improve yield prediction accuracy.
- **Deep Learning Models:** Experiment with LSTM (Long Short-Term Memory) networks for better time-series forecasting.
- **User Authentication:** Allow farmers to create profiles and save customized crop predictions based on their specific land sizes and regions.
- **Mobile Application:** Port the web platform to a mobile app for better accessibility in rural areas.

## 11. Conclusion
This project demonstrates the effective use of Machine Learning in the agricultural sector. By bridging the gap between historical agricultural data and modern predictive algorithms, it provides a valuable tool for maximizing crop yield, optimizing resources, and ensuring better financial planning for the agricultural community.
