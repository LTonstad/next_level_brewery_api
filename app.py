import pandas as pd

import streamlit as st

from brew_helpers import *       

def main():
    st.set_page_config(
        page_title="Open Brewery DB Exploration",
        page_icon=":beers:",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            "Get Help": "mailto:luke.tonstad@gmail.com",
            "Report a Bug": "https://github.com/LTonstad/next_level_brewery_api",
            "About": """
            ## This app uses the [Open Brewery DB API](https://www.openbrewerydb.org/)
            See the following link for [Documentation](https://www.openbrewerydb.org/documentation/)
            """,
        } # type: ignore
    )
    
    # User input as a streamlit form
    with st.form('query_form'):
        query_dict = {}
        header = st.columns([2,2])
        header[0].subheader('Text (Optional)')
        header[1].subheader('Type & Limit')
        
        row1 = st.columns([2,2,1])
        query_dict['name'] = row1[0].text_input('Brewery Name')
        query_dict['postal'] = row1[0].text_input('Brewery Postal')
        query_dict['city'] = row1[0].text_input('Brewery City')
        query_dict['state'] = row1[0].text_input('Brewery State')
        query_dict['country'] = row1[0].text_input('Brewery Country')
        query_dict['types'] = row1[1].multiselect(
            label = 'Brewery Type', 
            options=BREWERY_TYPES,
            default=None,
            help="Choosing none will allow for all brewery"
        )
        query_limit = row1[1].slider(
            'Limit', 
            min_value=5, max_value=100, step=5,
            help = "This selection will affect how many different breweries will return with search results"
        )
        
        query_submit = st.form_submit_button("Submit")
    
    if query_submit:
        condensed_query_dict = condense_query_dict(query_dict=query_dict)
        
        obdb_query = build_obdb_query(query_dict=condensed_query_dict, query_limit=query_limit, query_meta=False)
        obdb_meta_query = build_obdb_query(query_dict=condensed_query_dict, query_limit=query_limit, query_meta=True)
        
        # Sanity Checking
        st.markdown(f"Query being sent --> `{obdb_query}`")
        st.markdown(f"Metadata Query being sent --> `{obdb_meta_query}`")

        st.divider()
        
        # res = http_get(obdb_meta_query)
        # st.write(res)
        # Fetch Data
        df = pd.DataFrame(http_get(obdb_query)).set_index('id')
        df_meta = pd.DataFrame([http_get(obdb_meta_query)])
        
        # Display Data
        st.write("Metadata from parameters")
        st.dataframe(
            df_meta,
            use_container_width = True,
            hide_index = True
        )
        st.divider()
        st.write("Full from parameters")
        st.dataframe(
            df,
            use_container_width = True,
            hide_index = True
        )
        # Offer manipulation options
    
    
if __name__ == "__main__":
    main()