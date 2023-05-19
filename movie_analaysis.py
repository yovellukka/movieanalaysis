import streamlit as st
import csv
import os
import matplotlib.pyplot as plt
import pandas as pd

def home():
    st.title(':green[WE MAKE OUR CINEMA]:movie_camera:')
    st.write(":red[we make cinema is a subject that requires a combination of artistic creativity, technical know-how, and attention to detail. It's a collaborative effort that involves many skilled professionals, all working together to bring stories to life on the big screen and provide moviegoers with a high-quality cinematic experience.]")
    st.header('WE NEED YOU :hand:')
    st.write(":blue[The event will include a panel discussion, presentations, and networking opportunities with other industry professionals. We are confident that your participation would be an asset to our program, and we would be happy to provide any additional information you may need.\nPlease let us know at your earliest convenience if you are available to speak at our event. We look forward to hearing from you and hope that you will be able to join us.]")
    st.subheader("we need your support.please click"":red[_*my favorite thing in cinema*_]""and list your skill then submit")    
def main():
    options = ['Home','my favorite thing in cinema', 'overview']

    chosen_option = st.sidebar.radio('we make our cinema', options)

    if chosen_option == 'my favorite thing in cinema':
        user_page()
    elif chosen_option == 'overview':
        admin_page()
    else:
        home()

def user_page():
    st.title(':red[MY SKILL @]')
    story = st.selectbox('The Script/Story is', ['Below average', 'Average', 'Good', 'Excellent'])
    Direction = st.selectbox('The direction is...', ['Below average', 'Average', 'Good', 'Excellent'])
    DOP = st.selectbox('The DOP is...', ['Below average', 'Average', 'Good', 'Excellent'])
    Music = st.selectbox('The music is...', ['Below average', 'Average', 'Good', 'Excellent'])
    Editing = st.selectbox('The editor is...', ['Below average', 'Average', 'Good', 'Excellent'])
    age = st.slider('What is your age?', 0, 100, 15)

    if st.button('Submit'):
        data = {'age': age, 'story': story, 'direction': Direction, 'dop': DOP, 'music': Music, 'editing': Editing}
        file_path = 'movie2_data.csv'
        file_exists = os.path.exists(file_path)

        with open(file_path, 'a', -m, newline='') as csv_file:
            fieldnames = ['age', 'story', 'direction', 'dop', 'music', 'editing']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(data)

        st.write('Thank you for your responses! :sunglasses:')


def admin_page():
    st.title(':blue[OVERVIEW]')

    # Load survey data from a file or database
    file_path = 'movie2_data.csv'

    if os.path.exists(file_path):
        data = pd.read_csv(file_path)

    # Process the data and generate a plot
    plot_data = data.groupby('story')['age'].mean()
    plt.bar(plot_data.index, plot_data.values)
    plt.xlabel('Story')
    plt.ylabel('Average Age')
    st.pyplot()

    plot_data = data.groupby('direction')['age'].mean()
    plt.bar(plot_data.index, plot_data.values)
    plt.xlabel('Direction')
    plt.ylabel('Average Age')
    st.pyplot()

    plot_data = data.groupby('dop')['age'].mean()
    plt.bar(plot_data.index, plot_data.values)
    plt.xlabel('DOP')
    plt.ylabel('Average Age')
    st.pyplot()

    plot_data = data.groupby('music')['age'].mean()
    plt.bar(plot_data.index, plot_data.values)
    plt.xlabel('Music')
    plt.ylabel('Average Age')
    st.pyplot()

    plot_data = data.groupby('editing')['age'].mean()
    plt.bar(plot_data.index, plot_data.values)
    plt.xlabel('Editing')
    plt.ylabel('Average Age')
    st.pyplot()


if __name__ == '__main__':
    main()
    st.set_option('deprecation.showPyplotGlobalUse', False) 

