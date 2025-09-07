import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="IPL Win Probability Predictor",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced Custom CSS for modern UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f1419 0%, #1a2332 50%, #2d3748 100%);
        color: white;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 50%, #60a5fa 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 20px 40px rgba(59, 130, 246, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, transparent 100%);
        pointer-events: none;
    }
    
    .main-header h1 {
        font-size: 3.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        background: linear-gradient(0deg, #ffffff, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: #ffffff;
        background-clip: text;
    }
    
    .main-header p {
        font-size: 1.2rem;
        margin-top: 1rem;
        opacity: 0.9;
        font-weight: 400;
    }
    
    .input-section {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    }
    
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #60a5fa;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(96, 165, 250, 0.3);
        border-radius: 12px;
        color: white;
        backdrop-filter: blur(5px);
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #3b82f6;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
    }
    
    .stNumberInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(96, 165, 250, 0.3);
        border-radius: 12px;
        color: white;
        backdrop-filter: blur(5px);
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
        outline: none;
    }
    
    .predict-button {
        display: flex;
        justify-content: center;
        margin: 3rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: none;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1.2rem;
        padding: 1rem 3rem;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
        min-width: 250px;
        height: 60px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(59, 130, 246, 0.6);
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    .results-container {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 25px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
    }
    
    .probability-display {
        text-align: center;
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    
    .probability-high {
        background: linear-gradient(135deg, #059669 0%, #10b981 50%, #34d399 100%);
        box-shadow: 0 20px 40px rgba(16, 185, 129, 0.4);
    }
    
    .probability-medium {
        background: linear-gradient(135deg, #d97706 0%, #f59e0b 50%, #fbbf24 100%);
        box-shadow: 0 20px 40px rgba(245, 158, 11, 0.4);
    }
    
    .probability-low {
        background: linear-gradient(135deg, #dc2626 0%, #ef4444 50%, #f87171 100%);
        box-shadow: 0 20px 40px rgba(239, 68, 68, 0.4);
    }
    
    .probability-display::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .probability-number {
        font-size: 4rem;
        font-weight: 700;
        margin: 0.5rem 0;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
    }
    
    .team-name {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        opacity: 0.95;
    }
    
    .confidence-badge {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 0.9rem;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(5px);
        margin-top: 1rem;
    }
    
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        border-color: rgba(96, 165, 250, 0.5);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #60a5fa;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.8;
        font-weight: 500;
    }
    
    .strategy-message {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(37, 99, 235, 0.1) 100%);
        border-left: 4px solid #3b82f6;
        border-radius: 10px;
        padding: 1.5rem;
        margin-top: 2rem;
        backdrop-filter: blur(5px);
    }
    
    .strategy-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #60a5fa;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding: 2rem;
        opacity: 0.6;
        font-size: 0.9rem;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .element-container:has(style){
        display: none;
    }
    
    /* Input field placeholders */
    .stNumberInput input::placeholder {
        color: rgba(255, 255, 255, 0.5);
        opacity: 1;
    }
    
    /* Remove default values styling */
    .stNumberInput input[value=""] {
        color: rgba(255, 255, 255, 0.7);
    }
</style>
""", unsafe_allow_html=True)

# Load models
@st.cache_resource
def load_models():
    try:
        with open('models/win_probability_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('models/encoder.pkl', 'rb') as f:
            encoder = pickle.load(f)
        return model, encoder
    except FileNotFoundError:
        st.error("🚫 Model files not found. Please ensure 'win_probability_model.pkl' and 'encoder.pkl' are in the 'models' directory.")
        return None, None

# IPL team options
IPL_TEAMS = [
    'Chennai Super Kings',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Delhi Capitals',
    'Punjab Kings',
    'Rajasthan Royals',
    'Sunrisers Hyderabad',
    'Gujarat Titans',
    'Lucknow Super Giants'
]

# Prediction function
def predict_win_probability(model, encoder, team_name, runs, wickets, runs_required, balls_remaining, crr, rrr):
    input_data = pd.DataFrame([[team_name, runs, wickets, runs_required, balls_remaining, crr, rrr]],
                              columns=['chasing_team', 'runs', 'wickets', 'runs_required', 'balls_remaining', 'crr', 'rrr'])
    
    encoded = encoder.transform(input_data[["chasing_team"]])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(["chasing_team"]))
    input_data = pd.concat([input_data.drop(columns=["chasing_team"]), encoded_df], axis=1)
    
    win_prob = model.predict_proba(input_data)[:, 1][0]
    return win_prob

def get_strategy_message(prob_percentage, team_name, rrr, crr, wickets_left, balls_remaining):
    if prob_percentage > 50:
        if prob_percentage > 80:
            return f"🔥 **Excellent Position!** {team_name} is in a commanding position with {prob_percentage:.1f}% win probability. The required run rate ({rrr:.1f}) is manageable with {wickets_left} wickets in hand. Keep playing positively and rotate the strike!"
        elif prob_percentage > 70:
            return f"✨ **Strong Advantage!** {team_name} has a great chance of winning. With {wickets_left} wickets remaining, maintain the current approach and capitalize on loose deliveries. Victory is well within reach!"
        else:
            return f"👍 **Good Position!** {team_name} is ahead in this chase. Stay focused, build partnerships, and keep the scoreboard ticking. The momentum is in your favor!"
    else:
        if prob_percentage < 20:
            return f"⚡ **Time for Heroics!** {team_name} needs something special here. With only {prob_percentage:.1f}% win probability, it's time for aggressive batting. Target the boundaries, take calculated risks, and believe in the impossible!"
        elif prob_percentage < 35:
            return f"🎯 **Pressure Situation!** {team_name} needs to shift gears immediately. Required rate is {rrr:.1f} vs current rate of {crr:.1f}. Focus on strike rotation, find the gaps, and look for boundary opportunities every over!"
        else:
            return f"💪 **Fight Back Mode!** {team_name} is behind but still in the game! With {wickets_left} wickets left and {balls_remaining/6:.1f} overs remaining, build partnerships and accelerate gradually. Every run counts!"

# Main app
def main():
    # Main Header
    st.markdown("""
    <div class="main-header">
        <h1>🏏 IPL WIN PREDICTOR</h1>
        <p>AI for Real-time Match Analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load models
    model, encoder = load_models()
    
    if model is None or encoder is None:
        st.stop()
    
    # Input Section
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title"> Match Configuration</div>', unsafe_allow_html=True)
    
    # Create input columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        team_name = st.selectbox(
            "Chasing Team",
            IPL_TEAMS,
            index=0,
            help="Select the team batting second"
        )
        
        total_balls = st.number_input(
            "Total Balls in Innings",
            min_value=1,
            max_value=120,
            value=None,
            placeholder="Enter total balls (usually 120)",
            help="Total balls in the innings (20 overs = 120 balls)"
        )
        
        balls_faced = st.number_input(
            "Balls Faced",
            min_value=0,
            value=None,
            placeholder="Enter balls faced",
            help="Number of balls played so far"
        )
    
    with col2:
        runs = st.number_input(
            "Current Runs",
            min_value=0,
            value=None,
            placeholder="Enter current runs",
            help="Total runs scored by chasing team"
        )
        
        wickets = st.number_input(
            "Wickets Lost",
            min_value=0,
            max_value=10,
            value=None,
            placeholder="Enter wickets lost",
            help="Number of wickets down"
        )
    
    with col3:
        runs_required = st.number_input(
            "Runs Required",
            min_value=0,
            value=None,
            placeholder="Enter runs required",
            help="Runs needed to win the match"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Predict Button
    st.markdown('<div class="predict-button">', unsafe_allow_html=True)
    predict_clicked = st.button("🔮 PREDICT WIN PROBABILITY", use_container_width=False)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Results Section
    if predict_clicked:
        # Validation
        if any(val is None for val in [total_balls, balls_faced, runs, wickets, runs_required]):
            st.error("⚠️ Please fill in all fields to get prediction!")
            return
            
        # Calculate derived metrics
        balls_remaining = total_balls - balls_faced
        
        if balls_remaining <= 0:
            st.error("⚠️ No balls remaining! Match should be over.")
            return
        elif runs_required <= 0:
            st.success("🎉 Target already achieved! Win probability: 100%")
            return
        elif balls_faced <= 0:
            st.error("⚠️ Please enter valid balls faced (greater than 0)")
            return
            
        crr = (runs / balls_faced * 6) if balls_faced > 0 else 0
        rrr = (runs_required / balls_remaining * 6) if balls_remaining > 0 else 0
        
        try:
            # Make prediction
            win_prob = predict_win_probability(
                model, encoder, team_name, runs, wickets, 
                runs_required, balls_remaining, crr, rrr
            )
            
            prob_percentage = win_prob * 100
            wickets_left = 10 - wickets
            
            # Determine probability class and details
            if prob_percentage >= 70:
                prob_class = "probability-high"
                emoji = "🔥"
                status = "Excellent"
                confidence_color = "#10b981"
            elif prob_percentage >= 50:
                prob_class = "probability-medium" 
                emoji = "⚡"
                status = "Good"
                confidence_color = "#f59e0b"
            elif prob_percentage >= 30:
                prob_class = "probability-medium"
                emoji = "⚠️"
                status = "Challenging"
                confidence_color = "#f59e0b"
            else:
                prob_class = "probability-low"
                emoji = "🆘"
                status = "Critical"
                confidence_color = "#ef4444"
            
            # Results Container
            st.markdown('<div class="results-container">', unsafe_allow_html=True)
            
            # Main Probability Display
            st.markdown(f"""
            <div class="probability-display {prob_class}">
                <div class="team-name">{team_name}</div>
                <div class="probability-number">{prob_percentage:.1f}%</div>
                <div style="font-size: 1.1rem; margin: 1rem 0;">Win Probability {emoji}</div>
                <div class="confidence-badge" style="background-color: {confidence_color};">
                    {status} Situation
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Metrics Grid
            st.markdown('<div class="metrics-grid">', unsafe_allow_html=True)
            
            metrics = [
                ("⏱️", "Balls Remaining", balls_remaining, ""),
                ("📈", "Current Run Rate", f"{crr:.2f}", ""),
                ("🎯", "Required Run Rate", f"{rrr:.2f}", ""),
                ("🏏", "Wickets in Hand", wickets_left, ""),
                ("📊", "Runs per Ball Required", f"{runs_required/balls_remaining:.2f}", ""),
                ("⏰", "Overs Left", f"{balls_remaining/6:.1f}", "")
            ]
            
            for emoji_icon, label, value, unit in metrics:
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{emoji_icon}</div>
                    <div class="metric-value">{value}{unit}</div>
                    <div class="metric-label">{label}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Strategy Message
            strategy_msg = get_strategy_message(prob_percentage, team_name, rrr, crr, wickets_left, balls_remaining)
            
            if prob_percentage > 50:
                strategy_icon = "🎉"
                strategy_title = "Winning Strategy"
            else:
                strategy_icon = "💡"
                strategy_title = "Comeback Strategy"
            
            st.markdown(f"""
            <div class="strategy-message">
                <div class="strategy-title">
                    {strategy_icon} {strategy_title}
                </div>
                <p style="margin: 0; line-height: 1.6; font-size: 1rem;">{strategy_msg}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"❌ Error making prediction: {str(e)}")
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>🏏 Powered by AI | Built for Cricket Enthusiasts</p>
        <p>Real-time predictions • Strategic insights • Data-driven analysis</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()