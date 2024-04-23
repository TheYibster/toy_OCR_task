# OCR coding task for research position

This repository constitutes a coding problem aimed at assessing your ability to work with GitHub, Python, and basic OCR tools. You are welcome (and even encouraged to) use AI such as ChatGPT to help you with this, and please do not hesitate to reach out to annaboser@ucsb.edu if you have any questions about the problem or need a hint. We expect this will take you approximately 2 hours to complete. Email your solution to annaboser@ucsb.edu and ahilton@ucsb.edu by your interview time.

## Instructions: 

This problem requires you to digitize the numbers in the `data` folder of this directory. These numbers were pulled from a historical hydrological document like the one we would be working to digitize. To do so: 

1. Fork this repository to create your own to work out of. Make it a public repository. Clone it to your local computer. 
1. Create a `code/` folder. Write Python code in this folder which generates an `output.txt` file (housed in the main repository). This file will list all the numbers written on the images in the `data/` folder in the order of their image name (i.e. `image_1.png`, then `image_2.png`, etc.) , with a new number on each new line. 
1. Run your python code to generate the `output.txt` file. It's 100% fine if all the numbers are not correct. 
1. Document your work (see below for detailed instructions). Make sure everything is committed and pushed. 
1. Email a link you your completed forked repository to annaboser@ucsb.edu and ahilton@ucsb.edu by your interview time. Please ensure it is public so we can review it. 

### By the end of the problem, your repository should include: 
1. A `requirements.txt` or similar file with all the Python packages required to run your code specified and a filled out section to the readme (see below) with setup instructions such that I can easily recreate your environment and run your code
1. A `code` folder containing all the Python code necessary to generate the output file and a filled out section of the readme explaining these contents and how to run the code. Please additionally ensure that the code is properly commented and easily readable. 
1. The `output.txt` file containing the numbers printed on the documents in the data folder, in order and with a new line for each new entry. 

## Setup instructions 

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/TheYibster/toy_OCR_task.git

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt

## Instructions to reproduce the output

The `output.txt` file contained in this repository was generated with the code available in the `code/` folder. Simply run `main.py` within the `code/` folder.

    # make sure you are in the code/ directory
    cd code

Now, run the python script

    python main.py 

Or, on mac

    python3 main.py
