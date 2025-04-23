# Portfolio Website

This is a portfolio website built with Flask that showcases my projects, skills, and experience. The site includes separate pages for Home, About, Projects, and Contact, and features a responsive design with smooth animations, active navigation highlighting, and a downloadable resume.

## Features

- **Multi-page Layout:** Separate pages for Home, About, Projects, and Contact.
- **Responsive Design:** Fixed navbar with active page highlighting and a sticky, transparent footer.
- **Downloadable Resume:** The About page includes a button to download my resume as a PDF.
- **Smooth Animations:** Uses AOS (Animate On Scroll) for a modern, animated look.
- **GitHub Actions Deployment:** Automated deployment workflow to AWS.

## Technologies Used

- **Flask & Jinja2:** For building the dynamic web application and templating.
- **HTML, CSS, and JavaScript:** For layout, styling, and interactivity.
- **AOS (Animate On Scroll):** To add scroll-based animations.
- **Font Awesome:** For icons.
- **AWS S3/Elastic Beanstalk:** For hosting the site (static or dynamic deployment options).
- **GitHub Actions:** For CI/CD deployment workflow.

## Setup & Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
2. **Create and Activate a Virtual Environment:**
    ````bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. **Install Dependencies:**
    ````bash
    pip install -r requirements.txt
4. **Run the Application Locally:**
    ````bash
    python run.py 

## Deployment
This project uses GitHub Actions for automated deployment. The current workflow deploys a static version of the site to an AWS S3 bucket. If you prefer to deploy a dynamic Flask app (for example, using AWS Elastic Beanstalk), you’ll need to adjust the deployment configuration accordingly.

### For a Static Site (using Frozen-Flask)
1. **Build Static Files:**
    If you’re using Frozen-Flask, run:
    ````bash
    flask freeze
    This generates a dist/ folder with static files.

2. **GitHub Actions Workflow:**
The provided workflow in .github/workflows/deploy.yml does the following:
- Checks out the code.
- Sets up AWS credentials from repository secrets.
- Syncs the dist/ folder to your specified S3 bucket.
- Make sure to update the S3 bucket name in the workflow:

    ````yaml
    run: aws s3 sync dist/ s3://your-actual-bucket-name --delete

### For a Dynamic Flask App
If you need a dynamic deployment, consider deploying to AWS Elastic Beanstalk, Lightsail, or EC2. You can create a new workflow or modify the existing one to package and deploy your Flask app accordingly.

### Configuration
- Active Navigation:
  Each route passes an active_page variable to the templates so that the current page is highlighted in the navbar.

- Static Assets:
  All images, CSS, and JavaScript files are located in the static directory.

- Templates:
  All Jinja2 templates are stored in the templates directory.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes. If you encounter any issues or have suggestions, feel free to open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
If you have any questions or feedback, please contact me at your-email@example.com.