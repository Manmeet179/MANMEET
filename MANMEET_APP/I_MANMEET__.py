import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import streamlit as st
import time

# Set the page configuration with a custom theme
st.set_page_config(
    page_title="I_MANMEET__",
    page_icon="IMG/letter-m.png",
    layout="centered",  # You can change layout to wide if needed
    initial_sidebar_state="expanded",  # Sidebar can be either "expanded" or "collapsed"
)

# Customize your app using the lemon theme colors (for elements like buttons and text)
st.markdown("""
    <style>
        .css-1d391kg { background-color: #FFF8DC !important; }  /* Background */
        .css-1d391kg .css-16hu5mu { color: #000000 !important; } /* Text color */
        .css-1ck2b8r { background-color: #FFF700 !important; }  /* Primary color */
        .css-1v3fvcr { background-color: #F0E68C !important; }  /* Secondary background */
    </style>
""", unsafe_allow_html=True)



hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)


def main():
    with st.spinner('Loading...'):
        import time
        time.sleep(1)

        selected = option_menu(
            menu_title=None,
            options=['Home', 'Photography', 'About Me', 'Contact', 'Review'],
            icons=['house-fill', 'image-fill', 'person-square', 'envelope-fill', 'stars'],
            menu_icon="cast",
            default_index=0,  #
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "black"},
                "icon": {"color": "red", "font-size": "16px"},
                "nav-link": {
                    "margin-top": "-116px",
                    "font-size": "0px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#444",
                },
                "nav-link-selected": {"background-color": "white"},
            },
        )
        # st.markdown("<br><br>", unsafe_allow_html=True)

        menu_functions = {
            'Home': show_home,
            'Photography': show_photography,
            'About Me': show_about_me,
            'Contact': show_contact,
            'Review': show_review
        }

        if selected in menu_functions:
            menu_functions[selected]()


# henster
marquee_text = """
               <marquee behavior="scroll" direction="left" height="79px" scrollamount="16" style="color:red;">
    <style>
        .wheel-and-hamster {

            --dur: 2.5s;
            position: relative;
            width: 12em;
            height: 12em;
            font-size: 14px;
        }

        .wheel,
        .hamster,
        .hamster div,
        .spoke {
            position: absolute;
        }

        .wheel,
        .spoke {
            border-radius: 50%;
            top: 0;
            left: 0;
            width: -7%;
            height: 100%;
        }

        .wheel {
            background: radial-gradient(100% 100% at center,hsla(0,0%,60%,0) 47.8%,hsl(0,0%,60%) 48%);
            z-index: 2;
        }

        .hamster {
            animation: hamster var(--dur) ease-in-out infinite;
            top: -5%;
            left: calc(90% - 3.5em);
            width: 7em;
            height: 3.75em;
            transform: rotate(4deg) translate(-0.8em,1.85em);
            transform-origin: 50% 0;
            z-index: 1;
        }

        .hamster__head {
            animation: hamsterHead var(--dur) ease-in-out infinite;
            background: hsl(30,90%,55%);
            border-radius: 70% 30% 0 100% / 40% 25% 25% 60%;
            box-shadow: 0 -0.25em 0 hsl(30,90%,80%) inset,
                    0.75em -1.55em 0 hsl(30,90%,90%) inset;
            top: 0;
            left: -2em;
            width: 2.75em;
            height: 2.5em;
            transform-origin: 100% 50%;
        }

        .hamster__ear {
            animation: hamsterEar var(--dur) ease-in-out infinite;
            background: hsl(0,90%,85%);
            border-radius: 50%;
            box-shadow: -0.25em 0 hsl(30,90%,55%) inset;
            top: -0.25em;
            right: -0.25em;
            width: 0.75em;
            height: 0.75em;
            transform-origin: 50% 75%;
        }

        .hamster__eye {
            animation: hamsterEye var(--dur) linear infinite;
            background-color: hsl(0,0%,0%);
            border-radius: 50%;
            top: 0.375em;
            left: 1.25em;
            width: 0.5em;
            height: 0.5em;
        }

        .hamster__nose {
            background: hsl(0,90%,75%);
            border-radius: 35% 65% 85% 15% / 70% 50% 50% 30%;
            top: 0.75em;
            left: 0;
            width: 0.2em;
            height: 0.25em;
        }

        .hamster__body {
            animation: hamsterBody var(--dur) ease-in-out infinite;
            background: hsl(30,90%,90%);
            border-radius: 50% 30% 50% 30% / 15% 60% 40% 40%;
            box-shadow: 0.1em 0.75em 0 hsl(30,90%,55%) inset,
                    0.15em -0.5em 0 hsl(30,90%,80%) inset;
            top: 0.25em;
            left: 2em;
            width: 4.5em;
            height: 3em;
            transform-origin: 17% 50%;
            transform-style: preserve-3d;
        }

        .hamster__limb--fr2,
        .hamster__limb--fl1 {
            clip-path: polygon(0 0,100% 0,70% 80%,60% 100%,0% 100%,40% 80%);
            top: 2em;
            left: 0.5em;
            width: 1em;
            height: 1.5em;
            transform-origin: 50% 0;
        }




          .hamster__limb--fl1 {
            animation: hamsterFLLimb1 1.1s linear infinite;
            background: linear-gradient(hsl(30, 90%, 90%) 80%, hsl(0, 90%, 85%) 80%);
            transform: rotate(15deg);
        }

        @keyframes hamsterFLLimb1 {
            0%, 25%, 50%, 75%, 100% {
                transform: rotate(50deg);
            }
            12.5%, 37.5%, 62.5%, 87.5% {
                transform: rotate(-30deg);
            }
        }

        .hamster__limb--fr2 {
            animation: hamsterFRLimb2 1.1s linear infinite;
            background: linear-gradient(hsl(30, 90%, 80%) 80%, hsl(0, 90%, 75%) 80%);
            transform: rotate(15deg) translateZ(-1px);
        }

        @keyframes hamsterFRLimb2 {
            0%, 25%, 50%, 75%, 100% {
                transform: rotate(-30deg) translateZ(-1px);
            }
            12.5%, 37.5%, 62.5%, 87.5% {
                transform: rotate(50deg) translateZ(-1px);
            }
        }


        .hamster__limb--br,
        .hamster__limb--bl {
            border-radius: 0.75em 0.75em 0 0;
            clip-path: polygon(0 0,100% 0,100% 30%,70% 90%,70% 100%,30% 100%,40% 90%,0% 30%);
            top: 1em;
            left: 2.7em;
            width: 1.5em;
            height: 2.5em;
            transform-origin: 50% 50%;
        }

        .hamster__limb--br {
            animation: hamsterFRLimb2 1.1s linear infinite;
            background: linear-gradient(hsl(30,90%,80%) 90%,hsl(0,90%,75%) 90%);
            transform: rotate(-25deg) translateZ(-1px);
        }

        .hamster__limb--bl {
            animation: hamsterFLLimb1 1.1s linear infinite;
            background: linear-gradient(hsl(30,90%,90%) 90%,hsl(0,90%,85%) 90%);
            transform: rotate(-25deg);
        }

        .hamster__tail {
            animation: hamsterTail var(--dur) linear infinite;
            background: hsl(0,90%,85%);
            border-radius: 0.25em 50% 50% 0.25em;
            box-shadow: 0 -0.2em 0 hsl(0,90%,75%) inset;
            top: 1.5em;
            right: -0.5em;
            width: 1em;
            height: 0.5em;
            transform: rotate(30deg) translateZ(-1px);
            transform-origin: 0.25em 0.25em;
        }

        .spoke {
            animation: spoke var(--dur) linear infinite;
            background: radial-gradient(100% 100% at center,hsl(0,0%,60%) 4.8%,hsla(0,0%,60%,0) 5%),
                    linear-gradient(hsla(0,0%,55%,0) 46.9%,hsl(0,0%,65%) 47% 52.9%,hsla(0,0%,65%,0) 53%) 50% 50% / 99% 99% no-repeat;
        }

        /* Animations */
        @keyframes hamster {
            from, to {
                transform: rotate(4deg) translate(-0.8em,1.85em);
            }

            50% {
                transform: rotate(0) translate(-0.8em,1.85em);
            }
        }

        @keyframes hamsterHead {
            from, 25%, 50%, 75%, to {
                transform: rotate(0);
            }

            12.5%, 37.5%, 62.5%, 87.5% {
                transform: rotate(8deg);
            }
        }

        @keyframes hamsterEye {
            from, 90%, to {
                transform: scaleY(1);
            }

            95% {
                transform: scaleY(0);
            }
        }

        @keyframes hamsterEar {
            from, 25%, 50%, 75%, to {
                transform: rotate(0);
            }

            12.5%, 37.5%, 62.5%, 87.5% {
                transform: rotate(12deg);
            }
        }

        @keyframes hamsterBody {
            from, 25%, 50%, 75%, to {
                transform: rotate(0);
            }

            12.5%, 37.5%, 62.5%, 87.5% {
                transform: rotate(3deg);
            }
        }

        @keyframes hamsterFRLimb {
            from, 25%, 50%, 75%, to {
                transform: rotate(15deg);
            }

            12.5%, 37.5%, 62.5%, 87.5% {
                transform: rotate(-15deg);
            }
        }

        @keyframes hamsterFLLimb {
            from, 25%, 50%, 75%, to {
                transform: rotate(15deg);
            }

            12.5%, 37.5%, 62.5%, 87.5% {
                transform: rotate(-5deg);
            }
        }

        @keyframes hamsterBRLimb {
            from, 25%, 50%, 75%, to {
                transform: rotate(-25deg);
            }

            12.5%, 37.5%, 62.5%, 87.5% {
                transform: rotate(5deg);
            }
        }

        @keyframes hamsterBLLimb {
            from, 25%, 50%, 75%, to {
                transform: rotate(-25deg);
            }

            12.5%, 37.5%, 62.5%, 87.5% {
                transform: rotate(15deg);
            }
        }

        @keyframes hamsterTail {
            from, 25%, 50%, 75%, to {
                transform: rotate(30deg) translateZ(-1px);
            }

            12.5%, 37.5%, 62.5%, 87.5% {
                transform: rotate(45deg) translateZ(-1px);
            }
        }

        @keyframes spoke {
            100% {
                transform: rotate(1turn);
            }
        }
    </style>
    <div class="wheel-and-hamster">
        <div class="wheel">
            <div class="spoke"></div>
        </div>
        <div class="hamster">
            <div class="hamster__body">
                <div class="hamster__head">
                    <div class="hamster__ear"></div>
                    <div class="hamster__eye"></div>
                    <div class="hamster__nose"></div>
                </div>
                <div class="hamster__limb hamster__limb--fr2"></div>
                <div class="hamster__limb hamster__limb--fl1"></div>
                <div class="hamster__limb hamster__limb--br"></div>
                <div class="hamster__limb hamster__limb--bl"></div>
                <div class="hamster__tail"></div>
            </div>
        </div>
    </div>
  </marquee>
               """
st.markdown(marquee_text, unsafe_allow_html=True)

# code of pages
st.markdown("""
<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <style>
    body {
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
    .background-video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: -1;
    }
    .content {
        position: relative;
        z-index: 1;
        color: white; /* Adjust text color for contrast */
        padding: 20px;
        display: none;
    }
    .icon {
        font-size: 24px;
        color: #333; /* Default color */
        margin-right: 8px;
    }
    .github-icon {
        color: #333; /* GitHub color */
    }
    .instagram-icon {
        color: #E4405F; /* Instagram color */
    }
    .email-icon {
        color: #D44638; /* Email color */
    }
    .whatsapp-icon {
        color: #25D366; /* WhatsApp color */
    }
    .snapchat-icon {
        color: #FFFC00; /* Snapchat color */
    }
    .linkedin-icon {
        color: #0077b5; /* LinkedIn color */
    }
  </style>
</head>
<body>
  <video class="background-video" autoplay loop muted>
    <source src="C:/MY_PYTHON/PYTHON/vdo/4990249-hd_1920_1080_30fps.mp4" type="video/mp4">
  </video>
  <div class="content">
""", unsafe_allow_html=True)


def show_home():
    html_code = '''
        <style>
            /* Default styles */
            .container {
                position: relative;
                max-width: 100%;
                margin-top: 27px;
                text-align: center;
            }
            .header {
                font-size: 3rem;
                text-align: left;
                padding: 0px;
                margin: 0;
            }
            .icon {
                display: inline-block;
                width: 49px;
                vertical-align: middle;
                margin-top: -8px;
            }

            /* Responsive styles */
            @media (max-width: 768px) {
                .header {
                    font-size: 3rem;
                    padding: 15px;
                }
                .icon {
                    width: 49px;
                }
            }

            @media (max-width: 480px) {
                .header {
                    font-size: 1.6rem;
                    padding: 0px;
                }
                .icon {
                    width: 30px;
                    margin-top: -6px;
                }
            }
        </style>

        <div class="container">
            <h1 class="header">𝐌𝐄𝐄𝐓 𝐌𝐄𝐖𝐀𝐃𝐀 <img src="https://img.icons8.com/color/48/verified-badge.png" class="icon"/></h1>
        </div>
    '''

    # Display the HTML with styling
    st.markdown(html_code, unsafe_allow_html=True)

     st.markdown("---")

     st.subheader('I AM A DATA SCIENTIST 💻 & DATA ANALYST 📊🔍')

     st.markdown("---")
      # Blog link with bold text, emojis, and orange color
    blog_link = '''
    <p style="color:orange; font-weight:bold; font-size:20px;">
    🚀✨ <a href="https://manmeet179.blogspot.com/" target="_blank" style="color:orange; text-decoration:none;">
    Click to open my blog
    </a> ✨🚀
    </p>
    '''    
    # Display the link
    st.markdown(blog_link, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    **This blog serves as a showcase of my photography 📸 and offers a glimpse into who I am 🌟..**
    """)
    st.markdown("""
    Hi 👋🏻

I am Meet Mewada, though many prefer to call me Manmeet. I hail from the picturesque town of Vadgam, where I take immense pride in my heritage, particularly in my father’s exceptional craftsmanship as a highly skilled carpenter 🛠️. His unwavering dedication to his work has profoundly shaped my own values, instilling in me a strong sense of purpose and perseverance that guides me through every endeavor.

My academic journey has been marked by a rigorous pursuit of knowledge and excellence. I completed my Bachelor of Computer Applications (BCA) 🎓 at the esteemed Bhanumatiben Kantilal Mehta BCA & PGDCA College in Palanpur. This institution provided me with a robust foundation in computing 💻, where I engaged deeply with various technical disciplines including SOFTWERE DEVELOPMENT, DATA SCIENTIST 💻 & DATA ANALYST 📊🔍, and systems management. My academic focus was driven by an eagerness to master complex computing concepts and apply them in practical, impactful ways.

I laid the groundwork for my intellectual development at Smt. C.G. Mevada Higher Secondary School in Palanpur, also known as Vishwakarma Mevada School 🏫. This distinguished institution played a pivotal role in nurturing my academic curiosity and honing my analytical skills, setting the stage for my future pursuits. My interests are as diverse as they are fulfilling: I am captivated by the meticulous art of coin collecting 🪙, which connects me to a rich tapestry of cultural and historical narratives embedded within each artifact. Photography 📸 is another passion of mine, where I endeavor to capture and immortalize the aesthetic beauty of everyday moments, transforming ordinary scenes into extraordinary visual stories.

In my professional capacity as a Data Scientist and Analyst, I find immense satisfaction in tackling complex data challenges 👨🏻‍💻. My role involves intricate data scraping and web scraping tasks, where I meticulously gather and analyze data from various sources, leveraging my expertise in PostgreSQL and Python 🐍 to manage and interpret large datasets. This position allows me to deploy innovative solutions and insights that drive meaningful progress and enhance decision-making processes.

Beyond my professional and academic interests, I cherish engaging in thoughtful and stimulating conversations with friends 🗣️. These interactions not only foster deep connections but also provide opportunities to exchange ideas and broaden my understanding of diverse perspectives. My boundless curiosity fuels my exploration of the vast expanse of the internet 🌐, where I continuously seek out new knowledge, uncover emerging trends, and deepen my expertise across a myriad of fields.

Each of these aspects contributes to a well-rounded and fulfilling life, driven by a passion for learning, creativity, and meaningful connections.
    """)

    st.markdown("---")

    html_code = '''
        <div style="text-align: center; font-size: 14px; color: white;">
            Powered by~ 
            <span style="font-weight: bold;">MEET MEWADA</span>
            <img src="https://img.icons8.com/color/48/verified-badge.png" 
                 style="vertical-align: middle; margin-left: 0px; width: 14px; height: 14px; margin-top: -2px;"/>
        </div>
    '''

    # Display the HTML with styling
    st.markdown(html_code, unsafe_allow_html=True)


def show_photography():
    html_code = '''
        <style>
            .container {
                display: flex;
                align-items: center;
                justify-content: flex-start; /* Aligns title to the left */
                flex-wrap: wrap;
            }
            .header {
                font-size: 2rem;
                margin: 0;
                padding: 10px;
            }
            .icon {
                width: 44px;
                height: 44px;
                margin-left: -34px;
                margin-top: 6px;
            }

            /* Responsive Styles */
            @media (max-width: 768px) {
                .header {
                    font-size: 1.5rem;
                }
                .icon {
                    width: 30px;
                    height: 30px;
                    margin-left: -35px;
                    margin-top: 5px;
                }
            }

            @media (max-width: 480px) {
                .header {
                    font-size: 1.2rem;
                }
                .icon {
                    width: 30px;
                    height: 30px;
                    margin-left: -35px;
                    margin-top: 5px;
                }
            }
        </style>

        <div class="container">
            <h1 class="header">About My Photography</h1>
            <img src="https://img.icons8.com/color/48/ios-photos.png" class="icon"/>
        </div>
    '''

    # Display the HTML with styling
    st.markdown(html_code, unsafe_allow_html=True)

    st.markdown("---")
    # Display images
    st.image('IMG/1665242436382333-6.jpg', caption='⚡ Sustaining quiet strength in a world obsessed with noise.', use_column_width=True)
    st.image('IMG/1665242485508776-5.jpg', caption='🔥 Greatness is forged in the unseen chapters of discipline.', use_column_width=True)
    st.image('IMG/1665242495010057-4.jpg', caption='💪 The mind conquers long before the body follows.', use_column_width=True)
    st.image('IMG/1665242504531556-3.jpg', caption='🖤 Some memories remain because the soul refuses to forget.', use_column_width=True)
    st.image('IMG/1665242516063577-2.jpg', caption='⚡ Strength lies not in impulses, but in controlled chaos.', use_column_width=True)
    st.image('IMG/1665242525781967-1.jpg', caption='🚀 Every step forward begins with a battle within.', use_column_width=True)

    st.image('IMG/1665243271515329-12.jpg', caption='🏆 Consistency is the quiet architect of extraordinary outcomes.', use_column_width=True)
    st.image('IMG/1665243297809878-9.jpg', caption='🦁 A disciplined mind outperforms raw talent every single time.', use_column_width=True)
    st.image('IMG/1665243305672414-8.jpg', caption='🔥 Growth is uncomfortable, but stagnation is fatal.', use_column_width=True)
    st.image('IMG/1665243326888367-6.jpg', caption='💼 Every victory is first negotiated in silence.', use_column_width=True)
    st.image('IMG/1665243336409640-5.jpg', caption='🛡️ Loyalty remains rare because integrity is expensive.', use_column_width=True)
    st.image('IMG/1665243343667298-4.jpg', caption='🎯 When the vision is clear, explanations become unnecessary.', use_column_width=True)
    st.image('IMG/1665243353982227-3.jpg', caption='😎 Calmness is a form of power mastered by few.', use_column_width=True)
    st.image('IMG/1665243369272857-1.jpg', caption='🔥 Adversity refines a man the same way fire purifies metal.', use_column_width=True)
    st.image('IMG/1665243379503436-0.jpg', caption='🧠 A sharp mind perceives what the eyes overlook.', use_column_width=True)
    
    st.image('IMG/1665244157959326-7.jpg', caption='⏳ Progress is slow, but its consequences are monumental.', use_column_width=True)
    st.image('IMG/1665244175843069-5.jpg', caption='🌙 The night holds the clarity denied by daylight.', use_column_width=True)
    st.image('IMG/1665244199229803-1.jpg', caption='🌊 True strength flows quietly, never in haste.', use_column_width=True)
    
    st.image('IMG/1665244776167878-5.jpg', caption='🧩 Becoming the man I once sought in others.', use_column_width=True)
    st.image('IMG/1665244800876533-2.jpg', caption='🔥 Proving through action what words could never express.', use_column_width=True)
    
    st.image('IMG/1673956884456084-4.jpg', caption='🏹 Ambition guided by clarity becomes unstoppable.', use_column_width=True)
    st.image('IMG/1673956892717349-2.jpg', caption='🌤️ Healing begins when the mind accepts its own storms.', use_column_width=True)
    
    st.image('IMG/1674014863014743-6.jpg', caption='📈 Becoming a more refined version of myself each day.', use_column_width=True)
    st.image('IMG/1674014876448507-3.jpg', caption='🦅 Solitude sharpens a man’s vision more than any crowd ever will.', use_column_width=True)
    st.image('IMG/1674014880941829-2.jpg', caption='📸 Captured not in pose, but in purpose.', use_column_width=True)
    st.image('IMG/1674014885546496-1.jpg', caption='💙 Peace is achieved when the mind no longer negotiates with chaos.', use_column_width=True)
    st.image('IMG/1674014891015005-0.jpg', caption='⚔️ Pressure reveals character, not weakness.', use_column_width=True)
    
    st.image('IMG/1701065078712778-7.jpg', caption='🔥 My silence holds more intention than most conversations.', use_column_width=True)
    st.image('IMG/1701065083047910-6.jpg', caption='🎯 A simple exterior, a labyrinth of thoughts within.', use_column_width=True)
    
    st.image('IMG/IMG_20240127_213850.jpg', caption='💥 Strength wrapped in humility is a rare combination.', use_column_width=True)

    html_code = '''
            <div style="text-align: center; font-size: 14px; color: white;">
                Powered by~ 
                <span style="font-weight: bold;">MEET MEWADA</span>
                <img src="https://img.icons8.com/color/48/verified-badge.png" 
                     style="vertical-align: middle; margin-left: 0px; width: 14px; height: 14px; margin-top: -2px;"/>
            </div>
        '''

    # Display the HTML with styling
    st.markdown(html_code, unsafe_allow_html=True)

    # Add buttons


def show_about_me():
    html_code = '''
        <div style="display: flex; align-items: center;">
            <h1 style="margin-right: 10px;">About Me</h1>
            <img src="https://img.icons8.com/bubbles/100/about-me-male.png" 
                    style="width: 43px; height: 43px; margin-left: -36px; margin-top: 7px;"/>

        </div>
    '''

    # Display the HTML with styling
    st.markdown(html_code, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader('I AM A DATA SCIENTIST 💻 & DATA ANALYST 📊🔍')

    st.write("""



    I am the kind of individual whose very presence resonates with warmth 🌟, effortlessly radiating positivity ✨ to those around me. It’s not merely an aura but a conscious intention, a choice to infuse light 🌈 into every interaction and to leave an indelible impression on the hearts 💖 of those I meet. At the core of my being lies an unwavering foundation of kindness 💕, deeply rooted in empathy 🤗 and compassion, coupled with an unshakable loyalty that endures the test of time ⏳. These traits do not waver, no matter the circumstances; they are the pillars 🏛️ upon which my relationships are built, always standing firm, offering stability and reassurance to those who need it.

While my exterior may initially seem guarded, perhaps even enigmatic 🛡️, it is only a reflection of the depth within. For those willing to look beyond the surface, there is a reservoir of tenderness 🌷 and understanding waiting to be discovered. Once you break through the façade, you will find a friend who is not just present in moments of joy 🎉 but one who remains steadfast through the trials and tribulations of life, someone who stands unwavering beside you in both triumph 🏆 and turmoil 🌪️.

I see self-expression as an art form 🎨, and my sense of style is a reflection of my inner world. Every choice I make in how I present myself is deliberate, thoughtful, and an extension of my individuality 🦋. Whether it’s through my impeccable fashion sense 👗 or the subtle nuances of my demeanor, I believe that the way I carry myself speaks volumes before words are even exchanged.

My laughter is not just a sound but an experience—infectious in its sincerity 😂, it has a way of cutting through the noise and bringing genuine joy 😄 to those around me. I have an innate ability to find beauty 🌸 in the smallest of moments and to share that perspective with others, turning the mundane into something extraordinary. In this way, I become a source of light 💡, gently guiding others toward happiness and reminding them that even in darkness, there is always something worth smiling about 😊.

I am one of those rare souls 🌟 whose sweetness is not surface-level but runs deep, woven into the very fabric of my character. My presence lingers, not in the fleeting, momentary sense, but in the kind of way that leaves a lasting imprint on the soul 💫. The bonds I form are not mere connections—they are profound and transcendent 🌠, defying the limitations of time and circumstance. I do not take friendships or relationships lightly; they are treasures 🎁 to be cherished, nurtured, and preserved with care.

When I make you smile 😌, it is not merely an outward expression but one that stems from the very depths of your being, a smile that comes from a place of true connection and understanding. Once you come to know me, you’ll realize that letting go is not an option, for our bond is something that will feel irreplaceable 💞. In a world that is often transient and unpredictable, I offer something rare: a sense of constancy 🌍, a companionship that is not easily forgotten 💖.
    """)
    st.markdown("---")

    html_code = '''
            <div style="text-align: center; font-size: 14px; color: white;">
                Powered by~ 
                <span style="font-weight: bold;">MEET MEWADA</span>
                <img src="https://img.icons8.com/color/48/verified-badge.png" 
                     style="vertical-align: middle; margin-left: 0px; width: 14px; height: 14px; margin-top: -2px;"/>
            </div>
        '''

    # Display the HTML with styling
    st.markdown(html_code, unsafe_allow_html=True)


def show_contact():
    html_code = '''
       <button class="button" data-text="Awesome">
           <span class="actual-text">&nbsp;I_MANMEET__&nbsp;</span>
           <span aria-hidden="true" class="hover-text">&nbsp;I_MANMEET__&nbsp;</span>
       </button>

       <style>
       .button {
         margin: 0;
         height: auto;
         background: transparent;
         padding: 0;
         border: none;
         cursor: pointer;
       }

       .button {
         --border-right: 6px;
         --text-stroke-color: rgba(255,255,255,0.6);
         --animation-color: #37FF8B;
         --fs-size: 2em;
         letter-spacing: 3px;
         text-decoration: none;
         font-size: var(--fs-size);
         font-family: "Arial";
         position: relative;
         text-transform: uppercase;
         color: transparent;
         -webkit-text-stroke: 1px var(--text-stroke-color);
       }

       .hover-text {
         position: absolute;
         box-sizing: border-box;
         content: attr(data-text);
         color: var(--animation-color);
         width: 0%;
         inset: 0;
         border-right: var(--border-right) solid var(--animation-color);
         overflow: hidden;
         transition: 0.5s;
         -webkit-text-stroke: 1px var(--animation-color);
       }

       .button:hover .hover-text {
         width: 100%;
         filter: drop-shadow(0 0 23px var(--animation-color));
       }
       </style>
       '''
    st.components.v1.html(html_code, height=75)

    html_code = '''
        <div style="display: flex; align-items: center;">
            <h1 style="margin: 0;">Contact us</h1>
            <img src="https://img.icons8.com/external-soft-fill-juicy-fish/60/external-contact-envelopes-and-mail-soft-fill-soft-fill-juicy-fish.png" 
                 style="width: 39px; height: 39px; margin-left: -21px; margin-top: 17px;"/>
        </div>
    '''

    # Display the HTML with styling
    st.markdown(html_code, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    **Follow me on Instagram <a href="https://www.instagram.com/I_MANMEET__/" target="_blank"><i class="fab fa-instagram icon instagram-icon"></i></a>**
    """, unsafe_allow_html=True)
    st.markdown("""
    **Follow me on GitHub <a href="https://github.com/manmeet179/" target="_blank"><i class="fab fa-github icon github-icon"></i></a>**
    """, unsafe_allow_html=True)
    st.markdown("""
        **Email me <a href="mailto:manmeet2756@gamil.com"><i class="fas fa-envelope icon email-icon"></i></a>**
        """, unsafe_allow_html=True)

    # st.markdown("""
    # **Chat with me on WhatsApp <a href="https://wa.me/9081654122" target="_blank"><i class="fab fa-whatsapp icon whatsapp-icon"></i></a>**
    # """, unsafe_allow_html=True)
    st.markdown("""
    **Follow me on Snapchat <a href="https://www.snapchat.com/add/i_manmeet21" target="_blank"><i class="fab fa-snapchat-ghost icon snapchat-icon"></i></a>**
    """, unsafe_allow_html=True)
    st.markdown("""
    **Connect with me on LinkedIn <a href="https://www.linkedin.com/in/meet-mevada-3627b42b1?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank"><i class="fab fa-linkedin icon linkedin-icon"></i></a>**
    """, unsafe_allow_html=True)

    st.markdown("---")

    html_code = '''
            <div style="text-align: center; font-size: 14px; color: white;">
                Powered by~ 
                <span style="font-weight: bold;">MEET MEWADA</span>
                <img src="https://img.icons8.com/color/48/verified-badge.png" 
                     style="vertical-align: middle; margin-left: 0px; width: 14px; height: 14px; margin-top: -2px;"/>
            </div>
        '''

    # Display the HTML with styling
    st.markdown(html_code, unsafe_allow_html=True)


def show_review():
    html_code = '''
        <div style="display: flex; align-items: center;">
            <h1 style="margin: 0;">User Reviews</h1>
            <img src="https://img.icons8.com/fluency/48/ratings.png" 
                 style="width: 39px; height: 39px; margin-left: -24px; margin-top: 9px;"/>
        </div>
    '''

    # Display the HTML with styling
    st.markdown(html_code, unsafe_allow_html=True)

    st.markdown("---")

    reviews = [
        {"username": "@jaydip_patel", "name": "Jaydip Patel", "rating": 4.5, "caption": "Nice.. Brother ❤❤",
         "emoji": "🤟🏻⚡"},
        {"username": "@sanjaykp_12", "name": "Sanjay KP", "rating": 4.0, "caption": "Great effort! Well done.",
         "emoji": "👍🏻🔥"},
        {"username": "@priyanka_shah", "name": "Priyanka Shah", "rating": 5.0, "caption": "Amazing work! 🌟",
         "emoji": "🎉👏"},
        {"username": "@vikram_singh", "name": "Vikram Singh", "rating": 3.5, "caption": "Good, but can be improved.",
         "emoji": "🤔✨"},
        {"username": "@neha_gupta", "name": "Neha Gupta", "rating": 4.8, "caption": "Loved the attention to detail!",
         "emoji": "😍👌"},
        {"username": "@rahul_m", "name": "Rahul M", "rating": 4.9, "caption": "Fantastic experience!", "emoji": "🙌🔥"},
        {"username": "@riya_patel", "name": "Riya Patel", "rating": 5.0, "caption": "Exceeded my expectations!",
         "emoji": "💯🎯"},
        {"username": "@anuj_r", "name": "Anuj R", "rating": 4.2, "caption": "Quite impressive.", "emoji": "👏🏻😎"},
        {"username": "@meera_k", "name": "Meera K", "rating": 4.6, "caption": "Brilliant! Keep it up!", "emoji": "🌟🙌"},
        {"username": "@amit_b", "name": "Amit B", "rating": 4.0, "caption": "Great execution.", "emoji": "👍🏼🔥"},
        {"username": "@ananya_p", "name": "Ananya P", "rating": 3.9, "caption": "Good effort.", "emoji": "🙂✨"},
        {"username": "@krishna_m", "name": "Krishna M", "rating": 4.7, "caption": "Wonderful project!", "emoji": "🎉✨"},
        {"username": "@tina_s", "name": "Tina S", "rating": 4.1, "caption": "Nice work!", "emoji": "🙌🔥"},
        {"username": "@suresh_p", "name": "Suresh P", "rating": 4.5, "caption": "Impressive results.", "emoji": "💪🏻🔥"},
        {"username": "@geeta_d", "name": "Geeta D", "rating": 4.4, "caption": "Well done, great job!", "emoji": "👏🏻💯"},
        {"username": "@manish_r", "name": "Manish R", "rating": 4.0, "caption": "Neat execution.", "emoji": "👍🏻🎯"},
        {"username": "@asha_s", "name": "Asha S", "rating": 4.8, "caption": "Superb! Loved it!", "emoji": "😍👏"},
        {"username": "@tarun_k", "name": "Tarun K", "rating": 4.3, "caption": "Pretty good work.", "emoji": "🤝👍"},
        {"username": "@alka_j", "name": "Alka J", "rating": 4.6, "caption": "Fantastic job!", "emoji": "👏🏻🔥"},
        {"username": "@rohit_m", "name": "Rohit M", "rating": 4.7, "caption": "Remarkable project!", "emoji": "🌟🔥"},
        # New reviews
        {"username": "@dev_r", "name": "Dev R", "rating": 3.8, "caption": "Decent, could use some tweaks.",
         "emoji": "🔧💬"},
        {"username": "@isha_t", "name": "Isha T", "rating": 4.9, "caption": "Top-notch quality!", "emoji": "🌟👍"},
        {"username": "@karan_s", "name": "Karan S", "rating": 4.1, "caption": "Solid work. Keep it up!", "emoji": "👏🔥"},
        {"username": "@neelam_j", "name": "Neelam J", "rating": 4.4, "caption": "Very good, but some minor issues.",
         "emoji": "🛠️😊"},
        {"username": "@yash_p", "name": "Yash P", "rating": 4.6, "caption": "Great job, well executed.", "emoji": "💪👏"},
        {"username": "@manpreet_k", "name": "Manpreet K", "rating": 3.7,
         "caption": "Good effort, needs more refinement.", "emoji": "📝🔍"},
        {"username": "@ravi_g", "name": "Ravi G", "rating": 4.8, "caption": "Impressive work overall!", "emoji": "🎯💯"},
        {"username": "@sumit_s", "name": "Sumit S", "rating": 4.2, "caption": "Nice work, but can be enhanced.",
         "emoji": "👍💬"},
        {"username": "@neha_m", "name": "Neha M", "rating": 5.0, "caption": "Absolutely fantastic!", "emoji": "🌟🎉"},
        {"username": "@anil_b", "name": "Anil B", "rating": 4.5, "caption": "Well done, impressive results!",
         "emoji": "🔥💪"},
        {"username": "@mehul_s", "name": "Mehul S", "rating": 4.3, "caption": "Good job, but room for improvement.",
         "emoji": "👌🛠️"},
        {"username": "@sandeep_j", "name": "Sandeep J", "rating": 4.7, "caption": "Excellent execution!",
         "emoji": "👏🌟"},
        {"username": "@komal_d", "name": "Komal D", "rating": 3.6, "caption": "Average work, needs adjustments.",
         "emoji": "⚠️🔄"},
        {"username": "@pradeep_r", "name": "Pradeep R", "rating": 4.9, "caption": "Top quality and impressive.",
         "emoji": "🔥💯"},
        {"username": "@shivani_k", "name": "Shivani K", "rating": 4.0, "caption": "Good, but can be better.",
         "emoji": "👍💡"},
        {"username": "@krish_a", "name": "Krish A", "rating": 4.4, "caption": "Very good work, well done.",
         "emoji": "👏🌟"},
        {"username": "@neeraj_m", "name": "Neeraj M", "rating": 3.9,
         "caption": "Satisfactory, but some improvements needed.", "emoji": "🔄😌"},
        {"username": "@sanjana_r", "name": "Sanjana R", "rating": 4.7, "caption": "Great job, very satisfied!",
         "emoji": "🎉👏"},
        {"username": "@rohit_b", "name": "Rohit B", "rating": 4.6, "caption": "Fantastic work, very well done.",
         "emoji": "🌟🔥"},
        {"username": "@alisha_t", "name": "Alisha T", "rating": 4.1, "caption": "Nice work, but needs some tweaks.",
         "emoji": "🔧👍"},
        {"username": "@vinay_s", "name": "Vinay S", "rating": 4.8, "caption": "Excellent work, very impressed.",
         "emoji": "👏🌟"},
        {"username": "@sneha_r", "name": "Sneha R", "rating": 4.3, "caption": "Very good, could be better.",
         "emoji": "👍💬"},
        {"username": "@manoj_j", "name": "Manoj J", "rating": 4.9, "caption": "Outstanding performance!",
         "emoji": "💯👏"},
        {"username": "@anurag_p", "name": "Anurag P", "rating": 4.2, "caption": "Good job, needs minor improvements.",
         "emoji": "👌🔍"},
        {"username": "@isha_r", "name": "Isha R", "rating": 4.5, "caption": "Great effort, well executed.",
         "emoji": "🔥👏"},
        {"username": "@deepak_m", "name": "Deepak M", "rating": 4.0, "caption": "Satisfactory work, keep improving.",
         "emoji": "👍🔧"},
        {"username": "@pallavi_k", "name": "Pallavi K", "rating": 4.4, "caption": "Good work, but needs refinement.",
         "emoji": "👌💬"},
        {"username": "@manoj_s", "name": "Manoj S", "rating": 4.6, "caption": "Impressive job, well done!",
         "emoji": "👏🌟"},
        {"username": "@anita_d", "name": "Anita D", "rating": 4.3, "caption": "Nice work, could use more polish.",
         "emoji": "👍🔄"},
        {"username": "@arun_p", "name": "Arun P", "rating": 4.7, "caption": "Excellent work, very satisfied!",
         "emoji": "🎉👏"},
        {"username": "@bhavna_m", "name": "Bhavna M", "rating": 3.8,
         "caption": "Good job, but some improvements needed.", "emoji": "🔍🤔"},
        {"username": "@neeraj_s", "name": "Neeraj S", "rating": 4.2, "caption": "Well done, but needs minor tweaks.",
         "emoji": "👍🛠️"},
        {"username": "@nisha_r", "name": "Nisha R", "rating": 4.6, "caption": "Great effort, very impressed.",
         "emoji": "👏🔥"},
        {"username": "@rohit_s", "name": "Rohit S", "rating": 4.1, "caption": "Nice work, needs a bit of improvement.",
         "emoji": "👍🔧"},
        {"username": "@priya_s", "name": "Priya S", "rating": 4.8, "caption": "Fantastic work, keep it up!",
         "emoji": "🌟👏"},
        {"username": "@alok_t", "name": "Alok T", "rating": 4.0, "caption": "Good job, could be better.",
         "emoji": "👍💡"},
        {"username": "@seema_k", "name": "Seema K", "rating": 4.5, "caption": "Well done, great execution.",
         "emoji": "👏🌟"},
        {"username": "@amit_s", "name": "Amit S", "rating": 4.7, "caption": "Excellent job, very well done!",
         "emoji": "🌟🔥"},
        {"username": "@meenal_r", "name": "Meenal R", "rating": 3.9,
         "caption": "Satisfactory work, needs some changes.", "emoji": "🔄🙂"},
        {"username": "@sachin_m", "name": "Sachin M", "rating": 4.6, "caption": "Great work, very impressive.",
         "emoji": "👏💯"},
        {"username": "@tarun_p", "name": "Tarun P", "rating": 4.4, "caption": "Nice effort, needs some refinement.",
         "emoji": "👌🔧"},
        {"username": "@anjali_s", "name": "Anjali S", "rating": 4.3, "caption": "Good work, but can be improved.",
         "emoji": "👍💬"},
        {"username": "@gautam_r", "name": "Gautam R", "rating": 4.9, "caption": "Fantastic performance, very happy!",
         "emoji": "🎉👏"},
        {"username": "@praveen_s", "name": "Praveen S", "rating": 4.1, "caption": "Good effort, but some issues.",
         "emoji": "👍🔍"},
        {"username": "@anand_k", "name": "Anand K", "rating": 4.8, "caption": "Excellent work, very well done.",
         "emoji": "🌟🔥"},
        {"username": "@shweta_r", "name": "Shweta R", "rating": 4.2, "caption": "Nice work, needs some polish.",
         "emoji": "👍🔧"},
        {"username": "@rohit_j", "name": "Rohit J", "rating": 4.6, "caption": "Great job, very satisfied!",
         "emoji": "👏🔥"},
        {"username": "@isha_p", "name": "Isha P", "rating": 3.7, "caption": "Good effort, but needs more work.",
         "emoji": "🔄😌"},
        {"username": "@mohit_r", "name": "Mohit R", "rating": 4.5, "caption": "Well executed, very impressed.",
         "emoji": "🌟👏"},
        {"username": "@deepa_m", "name": "Deepa M", "rating": 4.3, "caption": "Nice work, but can be improved.",
         "emoji": "👍🔍"},
        {"username": "@ravi_s", "name": "Ravi S", "rating": 4.9, "caption": "Outstanding job, keep it up!",
         "emoji": "💯🌟"},
        {"username": "@priya_k", "name": "Priya K", "rating": 4.0, "caption": "Good work, needs minor adjustments.",
         "emoji": "👍🛠️"},
        {"username": "@mohit_s", "name": "Mohit S", "rating": 4.8, "caption": "Excellent work, very impressive.",
         "emoji": "🌟👏"},
        {"username": "@shilpa_r", "name": "Shilpa R", "rating": 4.2, "caption": "Nice job, could be better.",
         "emoji": "👍💡"},
        {"username": "@sonia_d", "name": "Sonia D", "rating": 4.6, "caption": "Great job, very happy with the results.",
         "emoji": "👏🌟"},
        {"username": "@gagan_s", "name": "Gagan S", "rating": 4.4, "caption": "Good work, needs some refinement.",
         "emoji": "👌🔧"},
        {"username": "@anil_s", "name": "Anil S", "rating": 3.8, "caption": "Satisfactory, but room for improvement.",
         "emoji": "🔄😊"},
        {"username": "@neelam_s", "name": "Neelam S", "rating": 4.7, "caption": "Excellent work, very satisfied!",
         "emoji": "🌟👏"},
        {"username": "@alisha_m", "name": "Alisha M", "rating": 4.5, "caption": "Great effort, well done.",
         "emoji": "👏🔥"},
        {"username": "@kiran_r", "name": "Kiran R", "rating": 4.3, "caption": "Good work, but needs more polish.",
         "emoji": "👍🔍"},
        {"username": "@shivani_j", "name": "Shivani J", "rating": 4.1, "caption": "Nice job, but needs improvement.",
         "emoji": "👍🔧"},
        {"username": "@ajay_k", "name": "Ajay K", "rating": 4.6, "caption": "Impressive work, very happy!",
         "emoji": "👏🔥"},
        {"username": "@pradeep_m", "name": "Pradeep M", "rating": 4.0, "caption": "Good, but can be improved.",
         "emoji": "👍🛠️"},
        {"username": "@sonia_s", "name": "Sonia S", "rating": 4.8, "caption": "Excellent job, very impressed.",
         "emoji": "🌟👏"},
        {"username": "@ankit_p", "name": "Ankit P", "rating": 4.3, "caption": "Good effort, but needs some work.",
         "emoji": "👌🔧"},
        {"username": "@divya_r", "name": "Divya R", "rating": 4.5, "caption": "Great job, well executed.",
         "emoji": "👏🌟"},
        {"username": "@rajesh_m", "name": "Rajesh M", "rating": 4.1, "caption": "Nice work, could be better.",
         "emoji": "👍🔍"},
        {"username": "@manish_s", "name": "Manish S", "rating": 4.6, "caption": "Fantastic work, very happy.",
         "emoji": "🌟🔥"},
        {"username": "@isha_m", "name": "Isha M", "rating": 4.2, "caption": "Good effort, needs minor adjustments.",
         "emoji": "👍🔧"},
        {"username": "@sumit_m", "name": "Sumit M", "rating": 4.9, "caption": "Excellent job, very impressive.",
         "emoji": "💯🌟"},
        {"username": "@neha_s", "name": "Neha S", "rating": 4.4, "caption": "Well done, but could be better.",
         "emoji": "👏🔍"},
        {"username": "@arun_r", "name": "Arun R", "rating": 4.8, "caption": "Great work, very satisfied!",
         "emoji": "🌟👏"},
        {"username": "@seema_s", "name": "Seema S", "rating": 4.3, "caption": "Good job, but needs more polish.",
         "emoji": "👍🔧"},
        {"username": "@mohit_k", "name": "Mohit K", "rating": 4.6, "caption": "Fantastic job, very impressed.",
         "emoji": "👏🔥"},
        {"username": "@asha_k", "name": "Asha K", "rating": 4.2, "caption": "Good work, needs a bit more refinement.",
         "emoji": "👍🔍"},
        {"username": "@ravi_m", "name": "Ravi M", "rating": 4.8, "caption": "Excellent work, very happy!",
         "emoji": "🌟👏"},
        {"username": "@anjali_r", "name": "Anjali R", "rating": 4.5, "caption": "Great job, very well executed.",
         "emoji": "👏🌟"},
        {"username": "@shiva_k", "name": "Shiva K", "rating": 4.3, "caption": "Good effort, could use some polish.",
         "emoji": "👍🔧"},
        {"username": "@sneha_p", "name": "Sneha P", "rating": 4.1, "caption": "Nice work, but needs improvement.",
         "emoji": "👍🔍"},
        {"username": "@deepa_s", "name": "Deepa S", "rating": 4.6, "caption": "Impressive job, very satisfied!",
         "emoji": "👏🌟"},
        {"username": "@manoj_m", "name": "Manoj M", "rating": 4.0, "caption": "Good work, but can be improved.",
         "emoji": "👍🔧"},
        {"username": "@shweta_k", "name": "Shweta K", "rating": 4.4, "caption": "Nice work, but needs some refinement.",
         "emoji": "👍🔧"},
        {"username": "@rajesh_k", "name": "Rajesh K", "rating": 4.7, "caption": "Great job, very impressed!",
         "emoji": "🌟👏"},
        {"username": "@pradeep_s", "name": "Pradeep S", "rating": 4.2, "caption": "Good effort, needs some tweaks.",
         "emoji": "👍🔧"},
        {"username": "@anita_r", "name": "Anita R", "rating": 4.5, "caption": "Great job, very happy with the results.",
         "emoji": "👏🌟"},
        {"username": "@sumit_s", "name": "Sumit S", "rating": 4.8, "caption": "Excellent work, keep it up!",
         "emoji": "🌟👏"},
        {"username": "@gagan_r", "name": "Gagan R", "rating": 4.6, "caption": "Impressive job, very satisfied!",
         "emoji": "👏🔥"},
        {"username": "@priyanka_r", "name": "Priyanka R", "rating": 4.3,
         "caption": "Good work, could use some improvements.", "emoji": "👍🔍"},
        {"username": "@seema_r", "name": "Seema R", "rating": 4.5, "caption": "Nice job, very happy with the outcome.",
         "emoji": "👏🌟"},
        {"username": "@anjali_m", "name": "Anjali M", "rating": 4.8, "caption": "Fantastic work, very impressive.",
         "emoji": "🌟👏"},
        {"username": "@neha_p", "name": "Neha P", "rating": 4.4, "caption": "Good effort, but needs more refinement.",
         "emoji": "👍🔧"},
        {"username": "@shilpa_m", "name": "Shilpa M", "rating": 4.6,
         "caption": "Great job, very satisfied with the results.", "emoji": "👏🌟"},
        {"username": "@manoj_p", "name": "Manoj P", "rating": 4.2, "caption": "Nice work, could use a bit more polish.",
         "emoji": "👍🔍"},
        {"username": "@neeraj_k", "name": "Neeraj K", "rating": 4.7, "caption": "Excellent job, very impressed!",
         "emoji": "🌟🔥"},
        {"username": "@isha_r", "name": "Isha R", "rating": 4.3, "caption": "Good effort, needs minor adjustments.",
         "emoji": "👍🔧"},
        {"username": "@pradeep_r", "name": "Pradeep R", "rating": 4.5,
         "caption": "Well done, very happy with the work.", "emoji": "👏🌟"},
        {"username": "@mohit_r", "name": "Mohit R", "rating": 4.4, "caption": "Nice job, but needs some fine-tuning.",
         "emoji": "👍🔍"},
        {"username": "@gagan_m", "name": "Gagan M", "rating": 4.8,
         "caption": "Excellent work, very happy with the outcome.", "emoji": "🌟👏"},
        {"username": "@deepa_p", "name": "Deepa P", "rating": 4.3,
         "caption": "Good work, but could use some improvements.", "emoji": "👍🔧"},
        {"username": "@shivani_m", "name": "Shivani M", "rating": 4.6, "caption": "Great job, very impressed!",
         "emoji": "👏🌟"},
        {"username": "@rohit_p", "name": "Rohit P", "rating": 4.2, "caption": "Nice effort, but needs some polish.",
         "emoji": "👍🔍"},
        {"username": "@ajay_m", "name": "Ajay M", "rating": 4.5,
         "caption": "Well executed, very happy with the results.", "emoji": "👏🌟"},
        {"username": "@sonia_k", "name": "Sonia K", "rating": 4.6, "caption": "Fantastic work, very satisfied.",
         "emoji": "🌟👏"},
        {"username": "@anil_k", "name": "Anil K", "rating": 4.4, "caption": "Good work, but could use some refinement.",
         "emoji": "👍🔧"},
        {"username": "@shilpa_k", "name": "Shilpa K", "rating": 4.7, "caption": "Excellent job, very impressive!",
         "emoji": "🌟🔥"},
        {"username": "@neha_m", "name": "Neha M", "rating": 4.3, "caption": "Nice work, but needs more polish.",
         "emoji": "👍🔍"},
        {"username": "@shivani_r", "name": "Shivani R", "rating": 4.8,
         "caption": "Great job, very happy with the outcome.", "emoji": "🌟👏"},
        {"username": "@anita_m", "name": "Anita M", "rating": 4.5, "caption": "Impressive work, well done!",
         "emoji": "👏🌟"},
        {"username": "@praveen_m", "name": "Praveen M", "rating": 4.6, "caption": "Fantastic work, very satisfied.",
         "emoji": "🌟👏"},
        {"username": "@deepak_r", "name": "Deepak R", "rating": 4.4, "caption": "Good job, but needs some fine-tuning.",
         "emoji": "👍🔍"},
        {"username": "@gagan_r", "name": "Gagan R", "rating": 4.7, "caption": "Excellent work, very happy!",
         "emoji": "🌟👏"},
        {"username": "@shivani_k", "name": "Shivani K", "rating": 4.8, "caption": "Great job, very impressive.",
         "emoji": "🌟👏"},
        {"username": "@neha_r", "name": "Neha R", "rating": 4.3, "caption": "Good work, needs a bit more refinement.",
         "emoji": "👍🔧"},
        {"username": "@pradeep_r", "name": "Pradeep R", "rating": 4.6, "caption": "Well done, very satisfied!",
         "emoji": "🌟👏"},
        {"username": "@sonia_r", "name": "Sonia R", "rating": 4.5, "caption": "Nice job, very pleased with the work.",
         "emoji": "👏🌟"},
        {"username": "@mohit_r", "name": "Mohit R", "rating": 4.2, "caption": "Good job, but needs some improvement.",
         "emoji": "👍🔧"},
        {"username": "@shivani_p", "name": "Shivani P", "rating": 4.7,
         "caption": "Great work, very happy with the result.", "emoji": "🌟👏"},
        {"username": "@deepa_k", "name": "Deepa K", "rating": 4.8, "caption": "Excellent job, very impressed!",
         "emoji": "🌟👏"}
    ]

    # Function to generate HTML for reviews dynamically
    def render_reviews_html(reviews):
        review_html = """
        <style>
            .review-container {
                display: flex;
                flex-direction: column;
                max-width: 600px;
                padding: 16px;
                border-radius: 10px;
                background-color: #f9f9f9;
                margin: 20px auto;
            }
            .reviewer-info {
                display: flex;
                align-items: center;
                margin-bottom: 12px;
            }
            .reviewer-name {
                font-size: 18px;
                font-weight: bold;
            }
            .review-rating {
                font-size: 16px;
                color: #ff9800;
            }
            .review-text {
                font-size: 16px;
                color: #333;
            }
        </style>
        """

        for review in reviews:
            review_html += f"""
            <div class="review-container">
                <div class="reviewer-info">
                    <div class="reviewer-name">{review['name']} ({review['username']})</div>
                </div>
                <div class="review-rating">Rating: {review['rating']} ⭐</div>
                <div class="review-text">{review['caption']} {review['emoji']}</div>
            </div>
            """

        return review_html

    # Generate the reviews HTML
    review_section_html = render_reviews_html(reviews)

    # Streamlit app

    # Display the reviews in Streamlit using HTML
    components.html(review_section_html, height=1000, scrolling=True)

    st.markdown("---")

    html_code = '''
            <div style="text-align: center; font-size: 14px; color: white;">
                Powered by~ 
                <span style="font-weight: bold;">MEET MEWADA</span>
                <img src="https://img.icons8.com/color/48/verified-badge.png" 
                     style="vertical-align: middle; margin-left: 0px; width: 14px; height: 14px; margin-top: -2px;"/>
            </div>
        '''

    # Display the HTML with styling
    st.markdown(html_code, unsafe_allow_html=True)


if __name__ == "__main__":
    main()











