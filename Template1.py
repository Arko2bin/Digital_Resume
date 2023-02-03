import streamlit as st
with open("profile.txt",'r') as source:
    contents = source.read().split("\n")
    profile_image = contents[1]
    name = contents[0]
st.set_page_config(page_title='Resume_' + name,layout="wide",page_icon=profile_image)
hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with st.container(): #Header Part name Image and about
    st.header(name)
    left,right = st.columns(2)
    with right:
        st.image(profile_image,width=100)
    with left:
        with open("about.txt","r") as about:
            st.write(about.read())
    st.write("---")

with st.container(): #Contact details skill experience education certification
    left,right = st.columns(2)
    with right: #contact details and certification
        st.header("	:telephone_receiver: Contact details: ")
        with open("contact.txt","r") as contact:
            for element in contact.read().split("\n"):
                try:
                    st.write(element.split(" - ")[0] + " : " + element.split(" - ")[1])
                except Exception:
                    pass
        with open("certificates.txt","r") as skills_cert: #technical skill
            flag = 0
            for skill_cert in skills_cert.read().split("\n"):
                skill = skill_cert.split(":-")[0]
                if(skill):
                    if(flag == 0):
                        st.header(":bulb: Skills")
                        flag = 1
                    else:
                        pass
                    with st.expander(":man-running: " + skill):
                        try:
                            certificates = skill_cert.split(":-")[1]
                            for certificate in certificates.split(","):
                                st.write(":reminder_ribbon: " + certificate.split("-")[0] + " : " + certificate.split("-")[1])
                        except Exception:
                            st.write(" ")
        with open("languages.txt","r") as lang_certs: #Languages
            flag = 0
            for lang_cert in lang_certs.read().split("\n"):
                lang = lang_cert.split(":-")[0]
                if(lang):
                    if(flag == 0):
                        st.header(":bulb: Languages Known")
                        flag = 1
                    else:
                        pass
                    with st.expander(lang):
                        try:
                            certificates = lang_cert.split(":-")[1]
                            for certificate in certificates.split(","):
                                st.write(":reminder_ribbon: " + certificate.split("-")[0] + " : " + certificate.split("-")[1])
                        except Exception:
                            st.write(" ")
    with left: #job experience and Education
        with open("experience.txt",'r') as experiences: #job experience
            flag = 0
            for experience in experiences.read().split("\n"):
                company = experience.split(":-")[0]
                if(company):
                    if(flag == 0):
                        st.header(":briefcase: Job Experiences")
                        flag = 1
                    else:
                        pass
                    with st.expander(":briefcase: " + company):
                        try:
                            works = experience.split(":-")[1]
                            for work in works.split(","):
                                st.write(":diamond_shape_with_a_dot_inside: " + work)
                        except Exception as e:
                            st.write(" ")
        with open("projects.txt",'r') as projects: #projects undertaken
            flag = 0
            for project in projects.read().split("\n"):
                project_name = project.split(":-")[0]
                if(project_name):
                    if(flag == 0):
                        st.header(":bulb: Project Experiences")
                        flag = 1
                    else:
                        pass
                    with st.expander(":bulb: " + project_name):
                        try:
                            works = project.split(":-")[1]
                            org_name = works.split(" : ")[0]
                            st.write(":office: " + org_name)
                            for work in works.split(" : ")[1].split(","):
                                st.write(":diamond_shape_with_a_dot_inside: " + work)
                        except Exception as e:
                            st.write(" ")
        st.header(":school: Education Background") #education
        with open("education.txt","r") as ed_certs:
            for ed_cert in ed_certs.read().split("\n"):
                school = ed_cert.split(":-")[0]
                with st.expander(":school: " + school):
                    try:
                        certificates = ed_cert.split(":-")[1]
                        for certificate in certificates.split(","):
                            st.write(certificate.split("-")[0] + " : " + certificate.split("-")[1])
                    except Exception:
                        st.write(" ")
