from functions import *
from configs import *


st.set_page_config(
    page_title="Thoughtlab Leave Portal",
    layout="centered",
    initial_sidebar_state="collapsed"
)


tab1, tab2 = st.tabs(["Applications", "Balances"])


with tab1:
    st.markdown('#### Pending applications')
    df = pd.DataFrame(np.random.randn(5, 5), columns=("col %d" % i for i in range(5)))

    st.table(df)

    
    options = st.multiselect(
    'Select applications numbers to approve/reject',
    ['Green', 'Yellow', 'Red', 'Blue'])

    if st.button("Approve", type="secondary"):
        if len(options) == 0:
            st.error("Please select at least one application to approve")
        else:
            st.write(f'you approved {options}')
    if st.button("Reject", type="secondary"):
        if len(options) == 0:
            st.error("Please select at least one application to reject")
        else:
            st.write(f'you rejected {options}')



    with tab2:


        
        st.markdown( '#### Leave balances - Last 12 Months')
        policy = st.multiselect(
            'Select a policy type ',
            ['Annual', 'Sick', 'Study', 'Unpaid'], 
            ['Annual', 'Sick', 'Study', 'Unpaid'])

        if len(policy)>0:
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.bar_chart(chart_data)
        else: 
            st.info('Select at least one leave policy to load chart')

        st.divider()

        st.markdown( '#### Dates on Leave')

        employees = st.multiselect(
            'Select a employee',
            ['user1', 'user2', 'user3', 'user4']
            )
        
        if len(employees) > 0:
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.bar_chart(chart_data)
        else: 
            st.info('Select at least one employee to load chart')