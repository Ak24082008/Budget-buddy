import streamlit as st
import math

# إعدادات الصفحة الرئيسية
st.set_page_config(
    page_title="Budget Buddy",
    page_icon="💰",
    layout="centered"
)

# ترويسة التطبيق (العنوان والوصف)
st.markdown("<h1 style='text-align: center; color: #D96B43;'>Budget Buddy 💰</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Plan your money, control your spending, and save smarter!</p>", unsafe_allow_html=True)

# إنشاء التبويبين المطلوبين
tab1, tab2 = st.tabs(["Budget Planner 💵", "Savings Goal 🎯"])

# ==========================================
# التبويب الأول: مخطط الميزانية الشهرية
# ==========================================
with tab1:
    st.header("Monthly Budget Planner")
    
    # إدخال الدخل الشهري
    income = st.number_input("Enter your monthly income (EGP):", min_value=0.0, value=2500.0, step=100.0)
    
    st.subheader("Plan Your Monthly Expenses")
    
    # تنظيم حقول المصاريف في 3 أعمدة كما في التصميم المطلوب
    col1, col2, col3 = st.columns(3)
    
    with col1:
        food = st.number_input("Food Budget:", min_value=0.0, value=400.0, step=50.0)
        transport = st.number_input("Transportation Budget:", min_value=0.0, value=250.0, step=50.0)
        
    with col2:
        education = st.number_input("Education Budget:", min_value=0.0, value=500.0, step=50.0)
        entertainment = st.number_input("Entertainment Budget:", min_value=0.0, value=200.0, step=50.0)
        
    with col3:
        shopping = st.number_input("Shopping Budget:", min_value=0.0, value=300.0, step=50.0)
        other = st.number_input("Other Expenses:", min_value=0.0, value=100.0, step=50.0)
        
    # زر الحساب بعرض كامل
    if st.button("Calculate My Budget", use_container_width=True, type="primary"):
        total_expenses = food + transport + education + entertainment + shopping + other
        remaining_balance = income - total_expenses
        
        st.divider()
        
        # عرض المؤشرات الثلاثة (Metrics)
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("Monthly Income", f"{income:,.0f} EGP")
        m_col2.metric("Planned Expenses", f"{total_expenses:,.0f} EGP")
        m_col3.metric("Remaining Balance", f"{remaining_balance:,.0f} EGP")
        
        # إظهار الرسالة المناسبة بناءً على النتيجة
        if total_expenses > income:
            st.error("⚠️ Warning: Your planned expenses are higher than your monthly income! Try reducing some costs.")
        elif total_expenses == income:
            st.warning("⚖️ Notice: You have used 100% of your monthly income. Nothing is left for savings.")
        else:
            st.success("✅ Great! You have money left to save.")

# ==========================================
# التبويب الثاني: حاسبة هدف الادخار
# ==========================================
with tab2:
    st.header("Savings Goal Calculator")
    st.write("Set a financial goal and find out how many months it will take to achieve it.")
    
    # مدخلات هدف الادخار
    goal_name = st.text_input("What are you saving for? (e.g., New Phone, Course, Trip):")
    target_amount = st.number_input("Target Amount (EGP):", min_value=0.0, value=0.0, step=500.0)
    monthly_saving = st.number_input("How much can you save each month? (EGP):", min_value=0.0, value=0.0, step=100.0)
    
    # زر حساب خطة الادخار
    if st.button("Calculate My Savings Plan", use_container_width=True, type="primary"):
        # التحقق من صحة المدخلات
        if not goal_name.strip() or target_amount <= 0:
            st.error("❌ Please complete the info: Enter a valid goal name and a target amount greater than zero.")
        elif monthly_saving <= 0:
            st.error("❌ Please enter a valid monthly saving amount greater than zero.")
        else:
            # حساب عدد الأشهر الصحيحة (تقريب لأعلى عدد صحيح)
            months_needed = math.ceil(target_amount / monthly_saving)
            
            st.divider()
            
            # عرض تفاصيل الهدف والنتائج
            st.subheader(f"🎯 Goal: {goal_name}")
            
            s_col1, s_col2, s_col3 = st.columns(3)
            s_col1.metric("Target Amount", f"{target_amount:,.0f} EGP")
            s_col2.metric("Monthly Saving", f"{monthly_saving:,.0f} EGP")
            s_col3.metric("Time Required", f"{months_needed} Month(s)")
            
            st.success(f"🎉 Awesome! If you save **{monthly_saving:,.0f} EGP** every month, you will reach your goal (**{goal_name}**) in **{months_needed} month(s)**!")

# ==========================================
# التذييل السفلي (Bottom Container / Footer)
# ==========================================
with st.bottom():
    st.markdown(
        "<div style='text-align: center; color: gray; font-size: 0.85em;'>"
        "Budget Buddy Challenge | Built with Python & Streamlit 💡"
        "</div>",
        unsafe_allow_html=True
    )