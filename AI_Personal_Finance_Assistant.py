import streamlit as st

# Define a dictionary of prompts and responses
responses = {
    "How can I create a budget?": "To create a budget, start by listing your income and expenses. Track your spending, set savings goals, and review your budget regularly.",
    "What is an emergency fund?": "An emergency fund is money set aside for unexpected expenses or financial emergencies. Aim to save 3-6 months' worth of living expenses.",
    "How do I track my expenses?": "Track your expenses using budgeting apps, spreadsheets, or by manually recording transactions. Categorize your spending to understand where your money goes.",
    "What are fixed and variable expenses?": "Fixed expenses are regular and consistent costs like rent or mortgage. Variable expenses fluctuate, such as groceries or entertainment.",
    "How much should I save for retirement?": "Aim to save at least 15% of your income for retirement. Adjust this based on your retirement goals and financial situation.",
    "What is a good savings goal?": "A good savings goal is to have an emergency fund, save for retirement, and set aside money for specific objectives like buying a home or vacation.",
    "How can I reduce my debt?": "To reduce debt, create a budget, cut unnecessary expenses, and make extra payments on high-interest debt. Consider consolidating debts if beneficial.",
    "What are some tips for saving money?": "Tips for saving money include creating a budget, tracking your spending, setting savings goals, and finding ways to reduce expenses.",
    "How often should I review my budget?": "Review your budget monthly to ensure you're staying on track. Adjust it based on changes in income or expenses.",
    "What is the 50/30/20 rule?": "The 50/30/20 rule suggests allocating 50% of your income to needs, 30% to wants, and 20% to savings and debt repayment.",
    "How can I improve my credit score?": "Improve your credit score by paying bills on time, reducing debt, keeping credit card balances low, and checking your credit report regularly for errors.",
    "What are some strategies for paying off student loans?": "Strategies include making extra payments, consolidating loans, refinancing for a lower interest rate, and exploring loan forgiveness programs.",
    "How can I save for a down payment on a house?": "Start by setting a savings goal, creating a dedicated savings account, cutting unnecessary expenses, and automating regular deposits into your savings.",
    "What is a sinking fund?": "A sinking fund is a savings fund for a specific purpose or goal, like a vacation or large purchase. Regularly contribute to this fund to reach your goal.",
    "How do I start investing?": "Begin investing by setting clear goals, understanding your risk tolerance, choosing an investment account, and researching investment options like stocks, bonds, and mutual funds.",
    "What is the difference between a 401(k) and an IRA?": "A 401(k) is an employer-sponsored retirement plan with potential employer matching. An IRA is an individual retirement account with tax benefits and more investment options.",
    "How can I set financial goals?": "Set financial goals by identifying your priorities, determining what you want to achieve, creating a plan, and tracking your progress regularly.",
    "What is the importance of diversification in investing?": "Diversification reduces risk by spreading investments across various asset classes. This helps protect your portfolio from significant losses in any one investment.",
    "How can I budget for irregular expenses?": "Create a separate savings fund for irregular expenses, estimate annual costs, divide by 12, and set aside that amount each month.",
    "What are the benefits of automatic savings?": "Automatic savings help you consistently save money without thinking about it. Set up automatic transfers to your savings account to ensure you meet your savings goals.",
    "How can I manage my finances during a financial crisis?": "During a financial crisis, prioritize essential expenses, review and adjust your budget, seek financial assistance if needed, and focus on rebuilding your emergency fund.",
    "What are some common budgeting mistakes to avoid?": "Common mistakes include not tracking expenses, failing to set realistic goals, neglecting to review and adjust the budget, and overspending in discretionary categories.",
    "How can I use financial apps to manage my budget?": "Financial apps help track expenses, categorize spending, set budgets, and monitor progress. Choose an app that fits your needs and integrates with your financial accounts.",
    "What should I include in a financial plan?": "A financial plan should include your financial goals, income, expenses, debt, savings, investments, insurance, and retirement planning."
}

# Streamlit app
st.set_page_config(page_title="Personal Finance Assistant", page_icon="💵", layout="wide")

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #e9ecef;
        border-right: 2px solid #ced4da;
    }
    .stTextInput input {
        border-radius: 8px;
        border: 2px solid #007bff;
        padding: 12px;
    }
    .stButton button {
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .stTitle {
        color: #003366; /* Darker color for visibility */
        font-size: 32px;
    }
    .stMarkdown {
        font-size: 18px;
    }
    .card {
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Header and description
st.markdown('<h1 class="stTitle">Personal Finance Assistant</h1>', unsafe_allow_html=True)
st.markdown("""
    <div class="card">
        Welcome to the Personal Finance Assistant! This tool provides answers to common personal finance questions.
        Use the dropdown menu below to select a question and receive detailed responses from our comprehensive guide.
    </div>
""", unsafe_allow_html=True)

# Create a dropdown menu for user to select prompts
selected_prompt = st.selectbox(
    "Select a question:",
    list(responses.keys()),
    format_func=lambda x: x.title()
)

# Provide a response based on selected prompt
if selected_prompt:
    response = responses.get(selected_prompt, "Sorry, I don't have an answer for that. Please try a different question.")
    st.markdown(f"<div class='card'><h2>Response:</h2><p>{response}</p></div>", unsafe_allow_html=True)

# Sidebar with additional info or links
st.sidebar.title("Additional Resources")
st.sidebar.markdown("""
    <div class="card">
        <h3>Useful Resources</h3>
        <ul>
            <li><a href="https://www.investopedia.com/terms/b/budget.asp" target="_blank">Budgeting Tips</a></li>
            <li><a href="https://www.moneyunder30.com/emergency-fund" target="_blank">Emergency Fund Guide</a></li>
            <li><a href="https://www.fidelity.com/learning-center/investment-strategies" target="_blank">Investment Strategies</a></li>
            <li><a href="https://www.nfcc.org/credit-debt/debt-management-tips/" target="_blank">Debt Reduction Tips</a></li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="card">
        ---
        <p><i>This tool is for educational purposes and should not be considered financial advice. Feel free to reach out for personalized advice from a financial expert.</i></p>
    </div>
""", unsafe_allow_html=True)
