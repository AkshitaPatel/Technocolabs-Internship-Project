import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('spotify_skip_prediction_model.pkl','rb'))



def predict(session_length,context_switch,
        no_pause_before_play, short_pause_before_play,
        long_pause_before_play, hist_user_behavior_n_seekfwd,
        hist_user_behavior_n_seekback,
        hour_of_day, premium, context_type_editorial_playlist,
        context_type_user_collection, context_type_radio,
        context_type_personalized_playlist, context_type_catalog,
        context_type_charts, hist_user_behavior_reason_start_trackdone,
        hist_user_behavior_reason_start_fwdbtn,
        hist_user_behavior_reason_start_backbtn,
        hist_user_behavior_reason_start_clickrow,
        hist_user_behavior_reason_start_appload,
        hist_user_behavior_reason_start_playbtn,
        hist_user_behavior_reason_start_remote,
        hist_user_behavior_reason_start_trackerror,
        hist_user_behavior_reason_start_endplay,
        hist_user_behavior_reason_end_trackdone,
        hist_user_behavior_reason_end_fwdbtn,
        hist_user_behavior_reason_end_backbtn,
        hist_user_behavior_reason_end_endplay,
        hist_user_behavior_reason_end_logout,
        hist_user_behavior_reason_end_remote, duration,
        us_popularity_estimate, acousticness, beat_strength, bounciness, 
        mechanism,speechiness, tempo,liveness,energy,flatness,mode, time_signature,
        day_of_week):
    
    input=np.array([[session_length,context_switch,
        no_pause_before_play, short_pause_before_play,
        long_pause_before_play, hist_user_behavior_n_seekfwd,
        hist_user_behavior_n_seekback,
        hour_of_day, premium, context_type_editorial_playlist,
        context_type_user_collection, context_type_radio,
        context_type_personalized_playlist, context_type_catalog,
        context_type_charts, hist_user_behavior_reason_start_trackdone,
        hist_user_behavior_reason_start_fwdbtn,
        hist_user_behavior_reason_start_backbtn,
        hist_user_behavior_reason_start_clickrow,
        hist_user_behavior_reason_start_appload,
        hist_user_behavior_reason_start_playbtn,
        hist_user_behavior_reason_start_remote,
        hist_user_behavior_reason_start_trackerror,
        hist_user_behavior_reason_start_endplay,
        hist_user_behavior_reason_end_trackdone,
        hist_user_behavior_reason_end_fwdbtn,
        hist_user_behavior_reason_end_backbtn,
        hist_user_behavior_reason_end_endplay,
        hist_user_behavior_reason_end_logout,
        hist_user_behavior_reason_end_remote, duration, 
        us_popularity_estimate, acousticness, beat_strength, bounciness, 
        mechanism,speechiness, tempo,liveness,energy,flatness,mode,
        day_of_week,time_signature]]).astype(np.float64)
    prediction=model.predict(input)
    return float(prediction)

def main():
    st.title("Spotify music skip prediction")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Spotify Skip Prediction ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    session_position = float(st.slider("Session position",1, 20,1))
    session_length = float(st.slider("Session length",10, 20,10))
    context_switch = float(st.slider("Context Switch",0, 1,0))
    no_pause_before_play = float(st.slider("No Pause before play",0, 1,0))
    short_pause_before_play = float(st.slider("Short pause before play",0, 1,0))
    long_pause_before_play = float(st.slider("Long pause before play",0, 1,0))
    hist_user_behavior_n_seekfwd = float(st.slider("Number of seek forward times",0, 60,0))
    hist_user_behavior_n_seekback = float(st.slider("Number of seek back times",0, 150,0))
#     hist_user_behavior_is_shuffle = float(st.slider("User encountered this track while shuffle was on",0, 1,0))
    hour_of_day = float(st.slider("Hour of the day",0, 23,0))
    premium = float(st.slider("Premium User",0, 1,0))
    
    context_type_editorial_playlist = 0.0
    context_type_user_collection = 0.0
    context_type_radio = 0.0
    context_type_personalized_playlist = 0.0
    context_type_catalog = 0.0
    context_type_charts = 0.0
    
    
    
    context_type = st.radio("what type of context the playback occurred within",('Editorial Playlist', 'User Collection', 'Radio','Personalized Playlist','Catalog','Charts'))
    
    if context_type=='Editorial Playlist':
        context_type_editorial_playlist=1.0
    elif context_type == 'User Collection':
        context_type_user_collection = 1.0
    elif context_type== 'Radio':
        context_type_radio = 1.0
    elif context_type== 'Personalized Playlist':
        context_type_personalized_playlist=1.0
    elif context_type=='Catalog':
        context_type_catalog = 1.0
    else:
        context_type_charts = 1.0
        
    
#     context_type_editorial_playlist = st.slider("Editorial Playlist?",0, 1,0)
#     context_type_user_collection = st.slider("User Collection?",0, 1,0)
#     context_type_radio = st.slider("Radio?",0, 1,0)
#     context_type_personalized_playlist = st.slider("Personalized Playlist?",0, 1,0)
#     context_type_catalog = st.slider("Catalog?",0, 1,0)
#     context_type_charts = st.slider("Charts?",0, 1,0)


    hist_user_behavior_reason_start_trackdone = 0.0
    hist_user_behavior_reason_start_fwdbtn = 0.0
    hist_user_behavior_reason_start_backbtn=0.0
    hist_user_behavior_reason_start_clickrow=0.0
    hist_user_behavior_reason_start_appload= 0.0
    hist_user_behavior_reason_start_playbtn= 0.0
    hist_user_behavior_reason_start_remote= 0.0
    hist_user_behavior_reason_start_trackerror= 0.0
    hist_user_behavior_reason_start_endplay= 0.0
    

    hist_user_behavior_reason_start = st.radio("The user action which led to the current track being played:",('Trackdone', 'Forward Button', 'Back Button','Click','Appload','Play Button','Remote','Track Error', 'End Play' ))
    
    if hist_user_behavior_reason_start == 'Trackdone':
        hist_user_behavior_reason_start_trackdone = 1.0
    elif hist_user_behavior_reason_start == 'Forward Button':
        hist_user_behavior_reason_start_fwdbtn = 1.0
    elif hist_user_behavior_reason_start == 'Back Button':
        hist_user_behavior_reason_start_backbtn = 1.0
    elif hist_user_behavior_reason_start == 'Click':
        hist_user_behavior_reason_start_clickrow = 1.0
    elif hist_user_behavior_reason_start == 'Appload':
        hist_user_behavior_reason_start_appload =1.0
    elif hist_user_behavior_reason_start == 'Play Button':  
        hist_user_behavior_reason_start_playbtn =1.0
    elif hist_user_behavior_reason_start == 'Remote':
        hist_user_behavior_reason_start_remote =1.0
    elif hist_user_behavior_reason_start == 'Track Error':  
        hist_user_behavior_reason_start_trackerror =1.0
    else:
        hist_user_behavior_reason_start_endplay =1
       
    
#     hist_user_behavior_reason_start_trackdone = st.slider("Reason to start is trackdone?",0, 1,0)
#     hist_user_behavior_reason_start_fwdbtn = st.slider("Reason to start is forward button?",0, 1,0)
#     hist_user_behavior_reason_start_backbtn= st.slider("Reason to start is back button?",0, 1,0)
#     hist_user_behavior_reason_start_clickrow= st.slider("Reason to start is click?",0, 1,0)
#     hist_user_behavior_reason_start_appload= st.slider("Reason to start is appload?",0, 1,0)
#     hist_user_behavior_reason_start_playbtn= st.slider("Reason to start is play button?",0, 1,0)
#     hist_user_behavior_reason_start_remote= st.slider("Reason to start is remote?",0, 1,0)
#     hist_user_behavior_reason_start_trackerror= st.slider("Reason to start is trackerror?",0, 1,0)
#     hist_user_behavior_reason_start_endplay= st.slider("Reason to start is endplay?",0, 1,0)

    hist_user_behavior_reason_end_trackdone= 0.0
    hist_user_behavior_reason_end_fwdbtn= 0.0
    hist_user_behavior_reason_end_backbtn= 0.0
    hist_user_behavior_reason_end_endplay= 0.0
    hist_user_behavior_reason_end_logout= 0.0
    hist_user_behavior_reason_end_remote= 0.0

    hist_user_behavior_reason_end = st.radio("The user action which led to the current track playback ending:",('Trackdone', 'Forward Button', 'Back Button','Remote','Logout', 'End Play' ))
    
    if hist_user_behavior_reason_end == 'Trackdone':
        hist_user_behavior_reason_end_trackdone = 1.0
    elif hist_user_behavior_reason_end == 'Forward Button':
        hist_user_behavior_reason_end_fwdbtn = 1.0
    elif hist_user_behavior_reason_end == 'Back Button':
        hist_user_behavior_reason_end_backbtn = 1.0
    elif hist_user_behavior_reason_end == 'Remote':
        hist_user_behavior_reason_end_remote =1.0
    elif hist_user_behavior_reason_end == 'End Play':  
        hist_user_behavior_reason_end_endplay =1.0
    elif hist_user_behavior_reason_end == 'Logout':
        hist_user_behavior_reason_end_logout =1.0  

    
#     hist_user_behavior_reason_end_trackdone= st.slider("Reason to end is trackdone?",0, 1,0)
#     hist_user_behavior_reason_end_fwdbtn= st.slider("Reason to end is forward button?",0, 1,0)
#     hist_user_behavior_reason_end_backbtn= st.slider("Reason to end is back button?",0, 1,0)
#     hist_user_behavior_reason_end_endplay= st.slider("Reason to end is end play?",0, 1,0)
#     hist_user_behavior_reason_end_logout= st.slider("Reason to end is logout?",0, 1,0)
#     hist_user_behavior_reason_end_remote= st.slider("Reason to end is remote?",0, 1,0)
    
    duration = float(st.slider("Duration",30, 1790,30))
#     release_year = float(st.slider("Release year",1950, 2018,1950))
    us_popularity_estimate= float(st.slider("US popularity estimate",90, 100,90))
    acousticness = float(st.slider("Acoustiness",0, 1,0))
    bounciness = float(st.slider("Bounciness",0, 1,0))
    beat_strength = float(st.slider("Beat strength",0, 1,0))
#     danceability = float(st.slider("Danceability",0, 1,0))
#     dyn_range_mean = float(st.slider("Dyn range mean",0, 1,0))
    energy = float(st.slider("Energy",0, 1,0))
    flatness = float(st.slider("Flaness",0, 1,0))
#     instrumentalness = float(st.slider("Instrumentalness",0, 1,0))
#     key = float(st.slider("Key",0, 11,0))
    liveness = float(st.slider("Liveness",0, 1,0))
#     loudness = float(st.slider("Loudness",-60, 1,-60))
    mechanism = float(st.slider("Mechanism",0, 1,0))
    mode = float(st.slider("Mode",0, 1,0))
#     organism = float(st.slider("Organism",0, 1,0))
    speechiness = float(st.slider("Speechiness",0, 1,0))
    tempo = float(st.slider("Tempo",0, 218,0))
    time_signature = float(st.slider("Time signature",0, 5,0))
#     valence = float(st.slider("Valence",0, 1,0))
    day_of_week = float(st.slider("Day of week", 0,6,0))
    
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Not Skipped</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Skipped</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict(session_length,context_switch,
        no_pause_before_play, short_pause_before_play,
        long_pause_before_play, hist_user_behavior_n_seekfwd,
        hist_user_behavior_n_seekback,
        hour_of_day, premium, context_type_editorial_playlist,
        context_type_user_collection, context_type_radio,
        context_type_personalized_playlist, context_type_catalog,
        context_type_charts, hist_user_behavior_reason_start_trackdone,
        hist_user_behavior_reason_start_fwdbtn,
        hist_user_behavior_reason_start_backbtn,
        hist_user_behavior_reason_start_clickrow,
        hist_user_behavior_reason_start_appload,
        hist_user_behavior_reason_start_playbtn,
        hist_user_behavior_reason_start_remote,
        hist_user_behavior_reason_start_trackerror,
        hist_user_behavior_reason_start_endplay,
        hist_user_behavior_reason_end_trackdone,
        hist_user_behavior_reason_end_fwdbtn,
        hist_user_behavior_reason_end_backbtn,
        hist_user_behavior_reason_end_endplay,
        hist_user_behavior_reason_end_logout,
        hist_user_behavior_reason_end_remote, duration,
        us_popularity_estimate, acousticness, beat_strength, bounciness, 
        mechanism,speechiness, tempo,liveness,energy,flatness,mode,
        day_of_week,time_signature)
#       st.success('The probability of user skipping the song is {}'.format(output))

        if output > 0.5 :
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()