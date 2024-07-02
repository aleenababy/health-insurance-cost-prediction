import streamlit as st
import joblib

def main():
    html_temp = """
    <div style = "background-color:lightblue;padding=16px">
    <h2 style = "color:black";text-align:center> Health Insurance Cost Predictor
    </div>
    
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    model = joblib.load('/Users/aleenababy/Documents/GitHub/health-insurance-cost-prediction/model_joblib_gr')
    p1 = st.slider("Enter your age", 18, 100)
    s1 = st.selectbox('Sex',('Male', 'Female'))
    if s1 =='Male':
        p2 = 1
    else:
        p2 = 0
    p3 = st.number_input("Enter your BMI(Body mass index) value")
    p4 = st.slider("Enter number of children",0, 5)
    s2 = st.selectbox("Are you a smoker? ", ("Yes", "No"))
    if s2 == "Yes":
        p5 = 1
    else:
        p5 = 0
    
    #p6 = st.slider("Enter your region", 1,4)#"southwest":0, "southeast":1, "northwest":2, "northeast":3
    s3 = st.selectbox("Enter your region", ("Southwest", "Southeast", "Northwest", "Northeast")) 
    if s2 == "Southwest":
        p6 = 0
    elif s2 == "Southeast":
        p6 = 1
    elif s3 == "Northwest":
        p6 = 2
    else:
        p6 = 3
    if st.button("Predict"):
        prediction = model.predict([[p1, p2, p3, p4, p5, p6]])   
        st.balloons() 
        st.success("your insurance cost is {} US Dollars".format(round(prediction[0],2)))
    
if __name__ == '__main__':
    main()