import streamlit as st
import numpy as np

def jarvis_ui(status="idle"):
    """
    Concentric neon circles for Jarvis.
    Status: idle, listening, processing, speaking
    """
    colors = {
        "idle": "#1abc9c",
        "listening": "#9b59b6",
        "processing": "#f39c12",
        "speaking": "#3498db"
    }
    color = colors.get(status, "#1abc9c")

    st.markdown(f"""
    <div style="display:flex; justify-content:center; align-items:center; height:400px; position:relative;">
        <div style="
            width:220px; height:220px; border-radius:50%;
            background: radial-gradient(circle, {color} 30%, #000 100%);
            box-shadow: 0 0 40px {color},0 0 80px {color},0 0 120px {color};
            animation: spin 2s linear infinite, pulse 1.5s ease-in-out infinite;
            position:absolute; top:0; left:0; right:0; bottom:0; margin:auto;"></div>
        <div style="
            width:160px; height:160px; border-radius:50%;
            border:5px solid {color};
            animation: rotate 1.5s linear infinite;
            position:absolute; top:0; left:0; right:0; bottom:0; margin:auto;"></div>
        <div style="
            width:100px; height:100px; border-radius:50%;
            border:3px solid {color};
            animation: rotate_reverse 2s linear infinite;
            position:absolute; top:0; left:0; right:0; bottom:0; margin:auto;"></div>
    </div>
    <style>
        @keyframes spin {{0%{{transform:rotate(0deg);}}100%{{transform:rotate(360deg);}}}}
        @keyframes pulse {{0%{{box-shadow:0 0 20px {color},0 0 40px {color},0 0 60px {color};}}
                           50%{{box-shadow:0 0 30px {color},0 0 60px {color},0 0 90px {color};}}
                           100%{{box-shadow:0 0 20px {color},0 0 40px {color},0 0 60px {color};}}}}
        @keyframes rotate {{0%{{transform:rotate(0deg);}}100%{{transform:rotate(360deg);}}}}
        @keyframes rotate_reverse {{0%{{transform:rotate(360deg);}}100%{{transform:rotate(0deg);}}}}
    </style>
    """, unsafe_allow_html=True)


def live_waveform(audio_chunk=None):
    """
    Real-time waveform for microphone input.
    audio_chunk: numpy array of audio amplitudes
    """
    if audio_chunk is None:
        audio_chunk = np.random.rand(100)  # random waveform for idle animation
    
    waveform_html = "".join([f"<div style='width:2px;height:{int(50*v+10)}px;background:#3498db;margin:1px;display:inline-block;'></div>" for v in audio_chunk])
    
    st.markdown(f"""
    <div style="display:flex; justify-content:center; align-items:flex-end; height:80px;">
        {waveform_html}
    </div>
    """, unsafe_allow_html=True)
