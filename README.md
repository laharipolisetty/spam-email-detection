This project demonstrates a spam email classification system using Natural Language Processing (NLP) and Machine Learning algorithms. The system classifies emails as either spam or ham (non-spam). This guide provides the steps to set up the environment, install dependencies, and run the application.

Steps to Set Up the Project
1. Open Anaconda Prompt
Launch the Anaconda Prompt from the Start Menu.

2. Check Available Conda Environments
To view all conda environments on your system, run:

conda env list

3. Check the Python Version
Verify the Python version installed in the current environment:

python --version

4. Create a New Conda Environment
Create a new conda environment with the desired Python version (e.g., Python 3.10):

conda create --name Spam_Class python=3.10

5. Activate the New Environment
Activate the newly created environment:

conda activate Spam_Class

6. Install Required Packages
Install the necessary libraries for your project:

pip install pandas

pip install scikit-learn

conda install ipykernel

pip install streamlit

7. Open VS Code
Launch Visual Studio Code (VS Code) to begin working on your project.

8. Create a Working Folder
Create a folder for your project, for example: AICTE_SPAM_PRO.

9. Open the Project Folder in VS Code
In VS Code, open the folder by navigating to:

File > Open Folder > Select the AICTE_SPAM_PRO folder

10. Create or Open a Jupyter Notebook
Create or open the notebook Spam Detector.ipynb in the project folder. Ensure the environment is set to Spam_Class in VS Code.

11. Train and Save the Model
Train the models and save it as spam123.pkl and vec123.pkl using the appropriate training scripts in your Jupyter Notebook.

12. Run the Streamlit Web Application
Create and run the Streamlit app using the file spamdetector.py. The app will classify email input as either spam or ham.

13. Open Integrated Terminal in VS Code
Open the integrated terminal in VS Code to run the application. Ensure the correct environment (Spam_Class) is activated.

14. Run the Streamlit App
Run the Streamlit app using the command:

streamlit run spamdetector.py

Troubleshooting
If there are any issues with the environment, ensure you have selected the correct environment (Spam_Class) in VS Code.

Conclusion
By following these steps, you can set up the environment, train the model, and deploy the spam email classifier using Streamlit.

File Names Used:
Spam Detector.ipynb: Jupyter notebook used for training and testing the model.
spam123.pkl: The saved trained model file.
vec123.pkl.pkl: The saved trained model file.
spamdetector.py: Python script for deploying the Streamlit web application.
