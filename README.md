# 🏏 IPL Win Probability Predictor

A sophisticated AI-powered web application that predicts win probabilities for IPL cricket matches in real-time using machine learning algorithms. Built with Streamlit and featuring a modern, interactive UI with glassmorphism design elements.

![IPL Predictor Demo](https://img.shields.io/badge/Status-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red) ![ML](https://img.shields.io/badge/ML-Scikit--Learn-orange)

App Link: [Live Demo](https://ipl-win-probability-predictor-tool.streamlit.app/)

## ✨ Features

### 🎯 Core Functionality
- **Real-time Win Probability Prediction** - AI-powered predictions based on current match state
- **All 10 IPL Teams Support** - Covers all current IPL franchises
- **Dynamic Strategy Insights** - Context-aware recommendations based on match situation
- **Comprehensive Match Metrics** - Current run rate, required run rate, balls remaining, and more

### 🎨 Modern UI/UX
- **Glassmorphism Design** - Beautiful translucent interface with blur effects
- **Responsive Layout** - Works seamlessly on desktop and mobile devices
- **Interactive Animations** - Smooth transitions and hover effects
- **Real-time Visual Feedback** - Color-coded probability indicators
- **Dark Theme** - Easy on the eyes with gradient backgrounds

### 📊 Advanced Analytics
- **Multi-factor Analysis** - Considers runs, wickets, balls remaining, and team performance
- **Confidence Indicators** - Visual representation of prediction reliability
- **Strategic Recommendations** - Tailored advice based on match situation
- **Performance Metrics Grid** - Comprehensive match statistics display

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/me-Afzal/IPL_win_probability_predictor.git
   cd IPL_win_probability_predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the models directory**
   ```bash
   mkdir models
   # Place your trained model files here:
   # - win_probability_model.pkl
   # - encoder.pkl
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501` to use the application.

## 📁 Project Structure

```
IPL_win_probability_predictor/
│
├── app/app.py                    # Main Streamlit application
├── models/                   # Machine learning models
│   ├── win_probability_model.pkl
│   └── encoder.pkl
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── Notebook.ipynb            # Jupyter notebook for model training
```

## 🛠️ Technology Stack

- **Frontend**: Streamlit with custom CSS
- **Backend**: Python
- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas, NumPy
- **UI Framework**: Custom CSS with glassmorphism design
- **Font**: Google Fonts (Inter)

## 📊 Model Information

The application uses a trained machine learning model that considers multiple factors:

### Input Features
- **Team Name** - The chasing team
- **Current Runs** - Runs scored so far
- **Wickets Lost** - Number of wickets down
- **Runs Required** - Runs needed to win
- **Balls Remaining** - Balls left in the innings
- **Current Run Rate** - Runs per over currently
- **Required Run Rate** - Runs per over needed

### Output
- **Win Probability** - Percentage chance of winning (0-100%)
- **Confidence Level** - Reliability indicator
- **Strategic Insights** - Contextual recommendations

## 🎮 How to Use

1. **Select the Chasing Team** from the dropdown menu
2. **Enter Match Details**:
   - Total balls in innings (usually 120 for T20)
   - Balls faced so far
   - Current runs scored
   - Wickets lost
   - Runs required to win
3. **Click "PREDICT WIN PROBABILITY"**
4. **View Results**:
   - Win probability percentage
   - Detailed match metrics
   - Strategic recommendations

## 🏏 Supported Teams

- Chennai Super Kings (CSK)
- Mumbai Indians (MI)
- Royal Challengers Bangalore (RCB)
- Kolkata Knight Riders (KKR)
- Delhi Capitals (DC)
- Punjab Kings (PBKS)
- Rajasthan Royals (RR)
- Sunrisers Hyderabad (SRH)
- Gujarat Titans (GT)
- Lucknow Super Giants (LSG)

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
scikit-learn>=1.3.0
pickle-mixin>=1.0.2
```

## 🎨 UI Features

### Visual Indicators
- 🔥 **Green (70%+)**: Excellent winning position
- ⚡ **Yellow (30-70%)**: Competitive situation
- 🆘 **Red (<30%)**: Critical situation requiring aggressive play

### Interactive Elements
- Hover effects on metric cards
- Animated probability displays
- Responsive button interactions
- Gradient backgrounds with shine effects

## 🚧 Development

### Adding New Features
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Model Updates
To update the machine learning model:
1. Train your new model
2. Save as `win_probability_model.pkl`
3. Update the encoder as `encoder.pkl`
4. Place in the `models/` directory

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Ensure you have the correct model files in place

## 🏆 Acknowledgments

- Thanks to the cricket data community for insights
- Streamlit team for the excellent framework
- IPL for providing exciting cricket matches to analyze

## 📈 Future Enhancements

- [ ] Player-specific impact analysis
- [ ] Weather condition integration
- [ ] Venue-based predictions
- [ ] Historical head-to-head analysis
- [ ] Live match integration via API
- [ ] Export predictions to PDF/CSV
- [ ] Multiple language support
- [ ] Mobile app version

---

**Made with ❤️ for Cricket Enthusiasts**

*Predict • Analyze • Strategize*