import config

# Define the functions for generating the files
def create_html_resume(data, path ):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{data['name']} - Resume</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>{data['name']}</h1>
                <p>{data['title']}</p>
                <p>{data['contact']['city']} • {data['contact']['phone']} • 
                <a href="mailto:{data['contact']['email']}">{data['contact']['email']}</a> • 
                <a href="{data['contact']['linkedin']}">LinkedIn</a> • 
                <a href="{data['contact']['github']}">GitHub</a></p>
            </div>
            <div class="section about">
                <h3>About Me</h3>
                <p>{data['about']}</p>
            </div>
            <div class="section experience">
                <h3>Professional Experience</h3>
        <div class="experience-item">
    """
    for job in data['experience']:
        html_content += f"""
            <h4>{job['position']} <span>{job['dates']}</span></h4>
            <p>{job['company']}, {job['location']}</p>
            <ul>
        """
        for detail in job['details']:
            html_content += f"<li>{detail}</li>"
        html_content += "</ul></div>"
    
    html_content += f"""
            <div class="section education">
                <h3>Education</h3>

                <p><strong>{data['education']['degree']}</strong> <br>
                {data['education']['institution']} <br>
                <em>{data['education']['dates']}</em></p>

                <p><strong>{data['education-2']['degree']}</strong> <br>
                {data['education-2']['institution']} <br>
                <em>{data['education-2']['dates']}</em></p>

            </div>
            """

    html_content += f"""
            <div class="section skills">
                <h3>Technical Skills</h3>
                <ul>
    """
    for skill in data['skills']:
        html_content += f"<li>{skill}</li>"
    
    html_content += """
                </ul>
            </div>
            <div class="section languages">
                <h3>Languages</h3>
                <ul>
    """

    for language in data['languages']:
        html_content += (
            f"<li><strong>{language['language']}:</strong> {language['certification']} "
            f"- <a href='{language['link']}' target='_blank'>View certificate: (Link)</a></li>\n"
        )
    
    html_content += f"""
                </ul>
            </div>
            <div class="footer">
                <button onclick="window.location.href='{data['resume_download_link']}';" class="download-btn">Download My Resume</button>
                <button onclick="window.location.href='{data['qr_code']}';" class="download-btn">Share this Profile</button>
                <button onclick="window.location.href='https://github.com/s33ding/my_resume/tree/main/my_certificates';" class="download-btn">View Certificates</button>
                <button onclick="window.location.href='{data['site_translated']}';" class="download-btn">Resume in Portuguese</button>
            </div>
        </div>
    </body>
    </html>
    """
    with open(path, "w") as file:
        file.write(html_content)



def create_html_resume_pt(data, path):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{data['name']} - Currículo</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>{data['name']}</h1>
                <p>{data['title']}</p>
                <p>{data['contact']['city']} • {data['contact']['phone']} • 
                <a href="mailto:{data['contact']['email']}">{data['contact']['email']}</a> • 
                <a href="{data['contact']['linkedin']}">LinkedIn</a> • 
                <a href="{data['contact']['github']}">GitHub</a></p>
            </div>
            <div class="About Me">
                <h3>Sobre Mim</h3>
                <p>{data['about']}</p>
            </div>
            <div class="section experience">
                <h3>Experiência Profissional</h3>
    """
    for job in data['experience']:
        html_content += f"""
            <h4>{job['position']}, <span>{job['dates']}</span></h4>
            <p>{job['company']}, {job['location']}</p>
        """
        for detail in job['details']:
            html_content += f"<li>{detail}</li>"
    
    html_content += f"""
            </div>
            <div class="section education">
                <h3>Formação Acadêmica</h3>
                <p><strong>{data['education']['degree']}</strong> <br>
                {data['education']['institution']} <br>
                <em>{data['education']['dates']}</em></p>

                <p><strong>{data['education-2']['degree']}</strong> <br>
                {data['education-2']['institution']} <br>
                <em>{data['education-2']['dates']}</em></p>

            </div>
            <div class="section skills">
                <h3>Competências Técnicas</h3>
                <ul>
    """
    for skill in data['skills']:
        html_content += f"<li>{skill}</li>"
    
    html_content += """
                </ul>
            </div>
            <div class="section languages">
                <h3>Idiomas</h3>
                <ul>
    """

    for language in data['languages']:
        html_content += (
            f"<li><strong>{language['language']}:</strong> {language['certification']} "
            f"- <a href='{language['link']}' target='_blank'>Ver certificado: (Link)</a></li>\n"
        )
    
    html_content += f"""
                </ul>
            </div>
            <div class="footer">
                <button onclick="window.location.href='{data['resume_download_link']}';" class="download-btn">Baixar meu Currículo</button>
                <button onclick="window.location.href='{data['qr_code']}';" class="download-btn">Compartilhar Este Perfil</button>
                <button onclick="window.location.href='https://github.com/s33ding/my_resume/tree/main/my_certificates';" class="download-btn">Ver Certificados</button>
                <button onclick="window.location.href='{data['site_translated']}';" class="download-btn">Currículo em Inglês</button>
            </div>
        </div>
    </body>
    </html>
    """
    with open(path, "w") as file:
        file.write(html_content)
